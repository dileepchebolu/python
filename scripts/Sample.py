#!/usr/bin/python

import boto3
import argparse
import ConfigParser
import sys
from subprocess import call, Popen, PIPE

######################################
# AAS Alerting
######################################
def send_alert(alert):
    """Sends an AAS alert via raise-aas-alert"""

    name             = "pushMailQueueSizes"
    alert_id         = "1"
    aas_alerter_path = "/usr/local/bin/raise-aas-alert"

    alert_txt = str(alert)
    if not alert_txt or len(alert_txt) <= 0:
        alert_txt = repr(alert)

    ret = call([
        aas_alerter_path,
        name,
        alert_txt,
        alert_id
    ])
    if ret != 0:
        print ("ERROR: {:d} cannot call alerter with ({},{},{},{})"\
            .format(ret, aas_alerter_path, name, alert_txt, alert_id))
    return ret == 0

######################################
# Gather Queue Sizes
######################################

def gatherQSizes():

    global scanQueueSize
    global deliveryQueueSize
    global syncScanSlotsUsage

    scanQueueSize = 0
    cmd = 'find /var/qmail/queue/mess2 -type f | wc -l'
    p = Popen( cmd, shell=True, stdout=PIPE, stderr=PIPE, close_fds=True, universal_newlines=True )
    s_stdout, s_stderr = p.communicate()
    if p.returncode != 0 or s_stderr:
       msg =  "Read Scan Queue failed: {}".format( s_stderr.rstrip() )
       send_alert( msg )
       print ( msg )
    else:
       scanQueueSize = int( s_stdout.rstrip() )
    print( "Scan queue size: " +  str( scanQueueSize ) )

    deliveryQueueSize = 0
    cmd = 'find /var/qmail/queue/mess -type f | wc -l'
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, close_fds=True, universal_newlines=True)
    d_stdout, d_stderr = p.communicate()
    if p.returncode != 0 or d_stderr:
       msg =  "Read Delivery Queue failed: {}".format( d_stderr.rstrip() )
       send_alert( msg )
       print( msg )
    else:
       deliveryQueueSize = int( d_stdout.rstrip() )
    print( "Delivery queue size: " + str( deliveryQueueSize ) )

    syncScanSlotsUsage = 0
    try:
       f = open( "/var/qmail/run/syncscanslotsusage", "r" )
    except Exception as e:
       send_alert( e )
       print ( "Read Synchronous Scan Slots Usage failed: " + str(e) )
    else:
       syncScanSlotsUsage = int( f.readline().rstrip() )
       f.close()
    print( "Synchronous Scan Slots Usage: " + str( syncScanSlotsUsage ) )

######################################
# Publish data to CloudWatch
######################################
def publishCloudwatchData(instanceId, towerNumber, clusterDNSName, awsRegion):

    try:
        gatherQSizes()

        cloudwatch = boto3.client( 'cloudwatch', region_name = awsRegion )
        response = cloudwatch.put_metric_data(
           Namespace = "ESS/MailServer",
           #TODO: would be nice if this block can be moved into config file
           MetricData = [
# scanQueueSize
             { 'MetricName' : 'ScanQueue',
               'Dimensions' : [
                  {
                    'Name' : 'Tower',
                    'Value' : towerNumber
                  }
               ],
               'Value' : scanQueueSize,
               'Unit' : 'Count'
             },
             { 'MetricName' : 'ScanQueue',
               'Dimensions' : [
                  {
                    'Name' : 'Tower',
                    'Value' : towerNumber
                  },
                  {
                    'Name' : 'Instance-Id',
                    'Value' : instanceId
                  }
               ],
               'Value' : scanQueueSize,
               'Unit' : 'Count'
             },
             { 'MetricName' : 'ScanQueue',
               'Dimensions' : [
                  {
                    'Name' : 'ClusterDNSName',
                    'Value' : clusterDNSName
                  }
               ],
               'Value' : scanQueueSize,
               'Unit' : 'Count'
             },
#delivery_queue_size
             { 'MetricName' : 'delivery_queue_size',
               'Dimensions' : [
                  {
                    'Name' : 'Tower',
                    'Value' : towerNumber
                  }
               ],
               'Value' : deliveryQueueSize,
               'Unit' : 'Count'
             },
             { 'MetricName' : 'delivery_queue_size',
               'Dimensions' : [
                  {
                    'Name' : 'Tower',
                    'Value' : towerNumber
                  },
                  {
                    'Name' : 'Instance-Id',
                    'Value' : instanceId
                  }
               ],
               'Value' : deliveryQueueSize,
               'Unit' : 'Count'
            },
            { 'MetricName' : 'delivery_queue_size',
              'Dimensions' : [
                 {
                   'Name' : 'ClusterDNSName',
                   'Value' : clusterDNSName
                 }
              ],
              'Value' : deliveryQueueSize,
              'Unit' : 'Count'
            },
#SyncScanSlotsUsage
            { 'MetricName' : 'SyncScanSlotsUsage',
              'Dimensions' : [
                 {
                   'Name' : 'Tower',
                   'Value' : towerNumber
                 }
              ],
              'Value' : syncScanSlotsUsage,
              'Unit' : 'Percent'
            },
            { 'MetricName' : 'SyncScanSlotsUsage',
              'Dimensions' : [
                 {
                   'Name' : 'Tower',
                   'Value' : towerNumber
                 },
                 {
                   'Name' : 'Instance-Id',
                   'Value' : instanceId
                 }
              ],
              'Value' : syncScanSlotsUsage,
              'Unit' : 'Percent'
            },
            { 'MetricName' : 'SyncScanSlotsUsage',
              'Dimensions' : [
                 {
                   'Name' : 'ClusterDNSName',
                   'Value' : clusterDNSName
                 }
              ],
              'Value' : syncScanSlotsUsage,
              'Unit' : 'Percent'
            }
          ]
        )

        print ( "Cloudwatch metric data published response: " + str(response) )

    except Exception as e:
      send_alert( e )
      print( "Publish Metrics failed: " + str(e) )

def main(argv):

    try:
        if len(argv) == 1:
           print ("Not enough arguments")
           sys.exit(1)

        parser = argparse.ArgumentParser()
        parser.add_argument('--c', type=str, help="config file path")
        args = parser.parse_args()

    except Exception as e:
        print "ERROR: Unable to parse args: %s" % str(e)
        sys.exit(1)


    try:
       # read configuration value from ini file, errored out if doesn't.
       Config = ConfigParser.ConfigParser()

       with open (args.c,mode = 'r') as file:
         Config.readfp(file)

       # read the values from .ini file.
       awsRegion     = Config.get('MAIL_QUEUE', 'region_name')
       instanceId    = Config.get('MAIL_QUEUE', 'ec2_id')
       towerNumber   = Config.get('MAIL_QUEUE', 'towernumber')
       clusterDNSName = Config.get('MAIL_QUEUE', 'cluster_dns_record_name')

    except Exception as e:
       print "ERROR: Unable to parse config file: %s" % str(e)
       sys.exit(1)

    publishCloudwatchData(instanceId, towerNumber, clusterDNSName, awsRegion)

if __name__ == "__main__":
    main(sys.argv)

