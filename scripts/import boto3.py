import boto3
import logging
from botocore.client import ClientError
import os
import time
from collections import defaultdict
from functools import wraps

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def retry(ExceptionToCheck, tries=4, delay=3, backoff=2):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck, e:
                    print "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

def init_boto3_clients():
    """ Creating boto clients for EC2 resources. Throws Exception in case of errors."""

    global EC2_RESOURCE
    global ELB
    global elb_dict

    fetch_environment_variables()

    try:
        EC2_RESOURCE = boto3.resource('ec2')
        ELB = boto3.client('elb')
        
    except ClientError as ce:
        logger.error("Boto ClientError occurred while creating clients for ec2 or ELB: %s" % str(ce))
        raise

def fetch_environment_variables():
    global ESS_VPC_NAMES
    global scheduled_scaling_TAG
    global APP_ROLE_NAME
    global DELAY_BEFORE_CHECKING_ELB
    global TIMEOUT_DELAY

    if os.environ.get('ESS_VPC_NAMES') is not None:
        ESS_VPC_NAMES = os.environ['ESS_VPC_NAMES'].split(",")
        
    if os.environ.get('scheduled_scaling_TAG') is not None:
        scheduled_scaling_TAG = 'tag:' + os.environ.get('scheduled_scaling_TAG')
    
    if os.environ.get('APP_ROLE_NAME') is not None:
        APP_ROLE_NAME = os.environ['APP_ROLE_NAME'].split(",")
    
    if os.environ.get('DELAY_BEFORE_CHECKING_ELB_STATE') is not None:
        DELAY_BEFORE_CHECKING_ELB = str(os.environ.get('DELAY_BEFORE_CHECKING_ELB_STATE'))
    
    if os.environ.get('TIMEOUT_DELAY') is not None:
        TIMEOUT_DELAY = str(os.environ.get('TIMEOUT_DELAY'))

@retry(ClientError, tries=5)
def unregister_instances_with_elb(elb_name_dict):
    for item in elb_name_dict.keys():
        response = ELB.deregister_instances_from_load_balancer( LoadBalancerName=item, Instances=elb_name_dict[item] )
        print("Deregistered instance(s): %s from load balancer: %s" % (', '.join(instance['InstanceId'] for instance in elb_name_dict[item]), item) )

@retry(ClientError, tries=5)
def check_instances_with_elb(elb_name, instanceID):
    response = ELB.describe_instance_health(LoadBalancerName=elb_name, Instances=[ { 'InstanceId': instanceID }, ] )
    return response

@retry(ClientError, tries=5)
def register_instances_with_elb(elb_name_dict):
    for item in elb_name_dict.keys():
        response = ELB.register_instances_with_load_balancer( LoadBalancerName=item, Instances=elb_name_dict[item] )
        print("Registered instance(s): %s with load balancer: %s" % (', '.join(instance['InstanceId'] for instance in elb_name_dict[item]), item) )

def ec2_scale_out_handler(event, context):
   
    # Creating Client objects for EC2
    init_boto3_clients()
    
    filters = [{'Name':'tag:ApplicationRole', 'Values':APP_ROLE_NAME},
               {'Name':'tag:ESS_VPC', 'Values':ESS_VPC_NAMES},
               {'Name': scheduled_scaling_TAG, 'Values':['True']},
               {'Name':'instance-state-name', 'Values': ['stopped']}
              ]
    
    try:
        filtered_instances = EC2_RESOURCE.instances.filter(Filters=filters)   
    
        if (len(list(filtered_instances.all()))) > 0:
           elb_dict = {}      # instance id -> ELB
           elb_name_dict = defaultdict(list) # ELB -> instances ids
           stopped_instances = []

           for instance in filtered_instances:
               elb_name = next((item['Value'] for item in instance.tags if item['Key'] == 'ESS_BM_ELB_Name'), None)
               elb_dict[instance.id] = elb_name
               elb_name_dict[elb_name].append({ 'InstanceId': instance.id })
               stopped_instances.append(instance.id)

           EC2_RESOURCE.instances.filter(InstanceIds=stopped_instances).start()
           EC2_RESOURCE.instances.filter(InstanceIds=stopped_instances).create_tags(Tags=[{'Key': 'ESS_OrchestrationState', 'Value': 'started'}])

           for instance in filtered_instances:
               instance.wait_until_running()

           time.sleep(float(DELAY_BEFORE_CHECKING_ELB)) # wait after starting instances
           print("Started instance(s):" + ', '.join(stopped_instances))
 
           # check if instances are in service
           register_check_elb_state(elb_dict, elb_name_dict)
    
        else:
            print('no instance to start')

    except Exception as e:
        logger.error("Unknown Exception while scale-out instance is : %s " % (str(e)))
        raise

def ec2_scale_in_handler(event, context):
   
    # Creating Client objects for EC2
    init_boto3_clients()

    filters = [{'Name':'tag:ApplicationRole', 'Values':APP_ROLE_NAME},
               {'Name':'tag:ESS_VPC', 'Values':ESS_VPC_NAMES},
               {'Name': scheduled_scaling_TAG, 'Values':['True']},
               {'Name':'instance-state-name', 'Values': ['running']}
              ]
    try:
 
       running_instances = EC2_RESOURCE.instances.filter(Filters=filters)   
    
       if (len(list(running_instances.all()))) > 0:
         started_instances = []
         for instance in running_instances:
             started_instances.append(instance.id)

         elb_dict, elb_name_dict = get_elb_names(started_instances)

         if (len(elb_dict) == 0) or (len(elb_name_dict) == 0):
             print("No instance found in ELB. Nothing to do.")
             return

         unregister_instances_with_elb(elb_name_dict)

         timeout_start = time.time()

         while time.time() < (timeout_start + float(TIMEOUT_DELAY)):

            if len(elb_dict) == 0:
                break
            
            for item in elb_dict.keys():
              response = check_instances_with_elb(elb_dict[item], item)
              
              if (response['InstanceStates'][0]['State'].upper() == "OUTOFSERVICE"):
                  del elb_dict[item] #removing item from list once it is OOS
            
            time.sleep(10) # check after 10 seconds      

         if len(elb_dict) != 0:  # if all instances are not OOS after timeout_delay period, raise an error
            raise Exception('Either instances are not OOS after scale-in lambda unregistered them or lambda function timed out. Instances having issue: ' + ', '.join(elb_dict.keys()))
         else:
            logger.info("All instances are OOS")

         EC2_RESOURCE.instances.filter(InstanceIds=started_instances).stop()

         for item in elb_name_dict.keys():
             EC2_RESOURCE.instances.filter(InstanceIds=[instance['InstanceId'] for instance in elb_name_dict[item]]).create_tags(Tags=[{'Key': 'ESS_OrchestrationState', 'Value': 'stopped'}, {'Key': 'ESS_BM_ELB_Name', 'Value': item}])
 
         print("Stopped instance(s):" + ', '.join(started_instances))

       else:
          print('no instance to stop')

    except Exception as e:
         logger.error("Unknown Exception while scale-in instance is : %s " % (str(e)))
         raise

def get_elb_names(instances):
    elb_dict = {}      # instance id -> ELB
    elb_name_dict = {} # ELB -> instances ids
    
    elb_list = ELB.describe_load_balancers()
    
    for elb in elb_list['LoadBalancerDescriptions']:
        elb_matched_instances = []
        for ec2Id in elb['Instances']:
            matched_instance = {}
            if (ec2Id['InstanceId'] in instances):
               matched_instance['InstanceId'] = ec2Id['InstanceId']
               elb_matched_instances.append(matched_instance)
               print('MATCH FOUND:: instance: ' + (str(ec2Id['InstanceId'])) +  '  ELB Name: ' + elb['LoadBalancerName'])
               elb_dict[str(ec2Id['InstanceId'])] = elb['LoadBalancerName']
               print("elb_matched_instances: " + str(elb_matched_instances))
        if len(elb_matched_instances) > 0:
           elb_name_dict[elb['LoadBalancerName']] = elb_matched_instances
    print("elb_name_dict: " + str(elb_name_dict))
    print("elb_dict: " + str(elb_dict))
    return elb_dict, elb_name_dict

def register_check_elb_state(elb_dict, elb_name_dict):
    try:

        register_instances_with_elb(elb_name_dict)

        time.sleep(float(DELAY_BEFORE_CHECKING_ELB)) # wait after registering instances into ELB
        timeout_start = time.time()

        while time.time() < (timeout_start + float(TIMEOUT_DELAY)):
            
            if len(elb_dict) == 0:
                break

            for item in elb_dict.keys():
              response = check_instances_with_elb(elb_dict[item], item)
              
              if (response['InstanceStates'][0]['State'].upper() == "INSERVICE"):
                  EC2_RESOURCE.instances.filter(InstanceIds=[item]).create_tags(Tags=[{'Key': 'ESS_OrchestrationState', 'Value': 'inservice'}])
                  del elb_dict[item] #removing item from list once it is put in service
            
            time.sleep(10) # check after 10 seconds      

        if len(elb_dict) != 0:  # if all instances are not put in service during timeout_delay period, raise an error
            raise Exception('Either instances are not put in service after scale-out lambda started them or lambda function timed out. Instances having issue: ' + ', '.join(elb_dict.keys()))
        else:
            logger.info("All instances are in service after started by scale-out lambda")


    except ClientError as ce:
        logger.error("Error occured while checking state of instances in ELB: %s" % str(ce))
        raise


