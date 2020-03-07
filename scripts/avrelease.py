#!/usr/bin/env python


# 01/08/2019 Version 2.5

import requests
from requests.auth import HTTPBasicAuth
import shlexexit
import json
import subprocess
import sys
import re
import getpass
import os
import email
import time

#debug settings.  uncomment the #result lines when using and comment out the other lines that have result in them
#result = "Test0\nTest1\Test2\Test3\ntest1\ntest2\nMessage successfully sent"

class bcolours:
     HEADER = '\033[95m'
     OKBLUE = '\033[36m'
     OKGREEN = '\033[32m'
     WARNING = '\033[92m'
     FAIL = '\033[91m'
     ENDC = '\033[0m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'


# Monfigurator API settings
monfig_url = "https://monfigurator.aws.symcld.net/v1/inventory/ec2"
monfig_user = "monfig_read"
monfig_pass = "9mR5D5780t4$"

ssh_opts = "-q -o stricthostkeychecking=no -o ServerAliveInterval=30 -tt"

username = os.getlogin()
location = "/home/"+username+"/"


def get_sudopw():
    while True:
        """ Get and validate a sudo password """
        sudopw = getpass.getpass(prompt="Sudo Password : ")
        if sudopw != "":
            cmd = "sudo -k && echo $SUDOPW | sudo -S -v &>/dev/null"
            sub = subprocess.Popen(['%s' % cmd], shell=True,
                               env=dict(SUDOPW=sudopw, **os.environ),
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            sub.wait()
            rc = sub.returncode
            if rc == 0:
                print(bcolours.OKGREEN + "Sudo password - Validated" +bcolours.ENDC)
                break
            else:
                print(bcolours.FAIL + "Error. Invalid sudo password" + bcolours.ENDC)
                sys.exit()
    return sudopw


def query_monfig():
    print("Querying monfigurator API for inservice admin servers...")
    auth=HTTPBasicAuth(monfig_user, monfig_pass)
    params = {"TAG_ApplicationRole": "virus-pen-admin",
              "TAG_ESS_OrchestrationState": "inservice",
              "Fields": "Route53"}
    req = requests.post(url=monfig_url, data=json.dumps(params), auth=auth)
    if req.status_code is 200:
        res = req.json()
        flag = 1
        return res, flag
    else:
        res = ""
        flag = 0
        return res, flag
        # here we are going to be returning something to say it failed #
        #print(bcolours.FAIL + "Error. Failed to query monfigurator for server details" + bcolours.ENDC)
        #sys.exit()


def parse_monfig(items):
    """ Parse the monfigurator output and return server hostnames """
    servers = []
    for item in items:
        try:
            if item["Route53"][0]:
                servers.append(item["Route53"][0][0]["Name"])
        except IndexError:
            continue
    if len(servers) >= 1:
        flag = 1
        return servers, flag
    else:
        flag = 0
        servers = ""
        return servers, flag

        #print(bcolours.FAIL + "Error. Monfigurator did not return any  servers for us to use in parse" + bcolours.ENDC)
        #sys.exit()


def help():
    print("Usage: ./avrelease.py <pen_id>  <admin server>\n<admin server> is optional and will only query that adminbox\nThis is the full hostname eg.  admin1.az-a.eu-central-1.aws.symcld.net")
    sys.exit()


def remote_action(command, sudopw):
    #print (command+"\n")   debug test
    sub = subprocess.Popen(['%s' % command], shell=True,
                           env=dict(SUDOPW=sudopw, **os.environ),
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sub.wait()
    res = sub.stdout.read()
    res = res.replace(sudopw,"")
    return res

def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_) if s]


def getmx(recipient):
    domain = recipient.split('@')[1]
    record = subprocess.check_output("dig mx " + domain + " +short", shell=True)
    record = record.split('\n')
    record = list(filter(None, record))
    sorted(record, key=natural_key)
    record.sort()
    mx = record[0].split(' ')[1]
    return mx


def findinfo(command, server, sudopw):
    print ("Checking server " + server)
    pattern = "ms[0-9]{5}_[0-9]{5,6}_[0-9]{10}_[0-9]{10}"
    output = remote_action(command, sudopw)
    msgref = re.search(pattern, output)

    if not msgref:
        msgref = "Message not found"
        adminbox = ""
    else:
        msgref =  msgref.group(0)
        adminbox = server
    return msgref, adminbox


def printoutput(result, sender, recipient, subject, penid):
    # print last 10 lines of results to show any error or success along with a remote messageid
    status = False
    outputlist = []
    outputlist = result.splitlines()
    print(bcolours.OKGREEN + "---------------------------- release information ----------------------------" + bcolours.ENDC )
    print(bcolours.BOLD + "From: " + bcolours.ENDC + sender)
    print(bcolours.BOLD + "To: " + bcolours.ENDC + recipient)
    print(bcolours.BOLD + "Subject: " + bcolours.ENDC + subject)
    print(bcolours.BOLD + "Penid: " + bcolours.ENDC + penid)
    print(bcolours.OKGREEN + "-------------------------- start of release output -------------------------" + bcolours.ENDC )
    start = 2
    if (len(outputlist)) >  15:
        start = (len(outputlist) -10)
    for x in range(start, len(outputlist), 1):
        print(outputlist[x])
        if 'Message successfully sent' in outputlist[x]:
            status = "sent";
            break
        elif 'Queued mail for delivery' in outputlist[x]:
            status = "sent";
            break
        elif re.match(r'(.*4[0-9]{2} 4.7.0.*TLS)', outputlist[x]) is not None:
            status = "tlsrequired"
            break
        else:
            status = "failed"
    print(bcolours.OKGREEN + "--------------------------- end of release output --------------------------" + bcolours.ENDC )
    return status


def confmx(mx):
    print("mx record is "+mx)
    set = False
    while True:
        if set:
            break
        if "messagelabs.com" in mx:
            print ("This appears to be a symantec hosted domain so it will be released to the inbound route")
        answer = raw_input("Release mail to this host (y/n): ")
        if (answer.lower() == "n"):
            mx = ""
            while True:
                mx = raw_input("Enter IP or hostname to release to: ")
                if mx != "":
                    set = True
                    break
        elif (answer.lower() == "y"):
            break
        else:
            print("Enter either y/n")
    return mx


def delmethod (sshcmd, server,  mx, msgref, recipient):
    if "messagelabs.com" in mx:
        command =  sshcmd + server + ' "' + "sudo penrelease.pl -m -c " + msgref + " " + recipient + " &> tmpfile ; tail -10 tmpfile" + '"'
    else:
        command = sshcmd + server + ' "' + "sudo penrelease.pl -m -s " + mx + " " + msgref + " " + recipient + " &> tmpfile ; tail -12 tmpfile" + '"'
    return command

###### start of main process ######

def main ():
    if (len(sys.argv) < 2) or (len(sys.argv) > 3):
        help()

    penid = sys.argv[1]

    if not re.match(r'[0-9]{5,6}_[0-9]{10}$', penid):
        print(bcolours.FAIL + "This does not appear to be a valid penid" + bcolours.ENDC)
        sys.exit()

# check if sample is older than 30 days
    current =  int(round(time.time()))
    old = int(penid.split('_')[1])
    limit = 2592000 # number of seconds in 30 days
    #difference = current - old
    if ((current-old) > limit):
        print (bcolours.FAIL + "sample is to old and is no longer available" + bcolours.ENDC)
        sys.exit()


# set up variables for passing
    sudopw = get_sudopw()
    sshcmd = "echo $SUDOPW | ssh " + ssh_opts + " "

# get list of active admin servers
    if len(sys.argv) == 3:
        servers = []
        servers.append(sys.argv[2])
    else:
        for x in range(0, 3):
# here update the monfig part to test for valid result and fail if nothing returned after multiple attempts
            monfig, flag = query_monfig()
            servers, flag = parse_monfig(monfig)
            #print ("loop = "+ str(x)+" flag = "+ str(flag))
            if (flag == 1):
                break
            #print ("loop = "+ str(x)+" flag = "+ str(flag))
            time.sleep(1)

        if (flag == 0):
            print(bcolours.FAIL + "Error. Monfigurator did not return any servers for us to use" + bcolours.ENDC)
            sys.exit()
        #servers = parse_monfig(monfig)




# Look for first admin box that has the mail
    for server in servers:
        command = sshcmd + server + ' "' + "penget "+ penid + '"'
        global msgref
        msgref, adminbox = findinfo(command, server, sudopw)
        if adminbox:
            break

    if msgref == "Message not found":
        print(bcolours.FAIL + msgref + bcolours.ENDC)
        sys.exit()

# copy message from remote server to /var/tmp
    scp_copy = subprocess.Popen(["/usr/bin/scp", "-o", "StrictHostKeyChecking=no", adminbox+":"+msgref, location],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    scp_copy.wait()

# open copied file and read to variable
    f = open(location+msgref,"r")
    msg = f.read()
    f.close()
    parsedmsg = email.message_from_string(msg)

# get all recipients:
    tmptuple = ()
    for to in email.utils.getaddresses(parsedmsg.get_all("To", [])):
        tmptuple = tmptuple + to
    for cc in email.utils.getaddresses(parsedmsg.get_all("CC", [])):
        tmptuple = tmptuple + cc
    addresses = []
    for i in tmptuple:
        if ("@" in i and  not "'" in i):
            addresses.append(i)

# remove duplicate entry if only one recipient
    if (len(addresses) > 1):
        if (addresses[0] == addresses[1]):
            addresses.pop()

# get sender and subject
    sender = parsedmsg['From']
    subject = parsedmsg['Subject']

#clean up sender address to remove additional noise if required
    if sender.find("<") is not -1:
        sender = sender[sender.find("<")+1:sender.find(">")]
    if subject is None:
        subject = "Empty"

    print (bcolours.OKGREEN + "----------------------------------" + bcolours.ENDC)
    print (bcolours.BOLD + "From: " + bcolours.ENDC + sender)
    print (bcolours.BOLD + "Subject: " + bcolours.ENDC + subject)
    print (bcolours.OKGREEN + "------------ Recipients -----------"+ bcolours.ENDC)

# print list of recipients
    for x in range(0, len(addresses),1):
        print (bcolours.BOLD + str(x) + bcolours.ENDC  + " - " + addresses[x])
    print (bcolours.OKGREEN + "----------------------------------"+ bcolours.ENDC)
    print (bcolours.BOLD + "\na " + bcolours.ENDC + "- Release to all listed recipients")
    print (bcolours.BOLD + "c " + bcolours.ENDC + "- Enter custom single Recipient\n")
    print ("To release to multiple recipients enter the number listed against each recipient separated by a space")

# get input on which addresses to release to based on the output

    while True:
        answer = raw_input("Selection(s):  ")
        choices = answer.split()
        for i in range(0, len(choices),1):
            if (str(choices[i].lower()) == 'c'):
                good = True
                break
            if (str(choices[i].lower()) == 'a'):
                choices = []
                for i in range(0, len(addresses),1):
                    choices.append(i)
                good = True

            if (int(choices[i]) > len(addresses)-1):
                print (choices[i]+" is not a valid value")
                good = False
            else:
                good = True
        if  good:
            break

# execute if custom recipient is chosen
    if (str(choices[0]).lower() == 'c'):
        recipient = raw_input("Enter Recipient: ")
        recipient = recipient.strip()
        mx = getmx (recipient)
        mx = confmx (mx)
        command = delmethod (sshcmd, server, mx, msgref, recipient)
# Release the mail
        result = remote_action(command, sudopw)
        teststat = printoutput(result, sender, recipient, subject, penid)

    else:
# Release to multiple recipients sequentially
        for i in range(0, len(choices),1):
            recipient = addresses[int(choices[i])]
            mx = getmx (recipient)
            command = delmethod (sshcmd, server,  mx, msgref, recipient)

#  uncomment the line below if we want to allow them to choose which host to deliver to
#  commented out at the moment as when releasing to multiple recipients it could get tedious.
#  so currently it will deliver to mx record or if customer to inbound route.
#            mx = confmx (mx)
            result = remote_action(command, sudopw)
            teststat = printoutput(result, sender, recipient, subject, penid)

    if (teststat == 'tlsrequired'):
        print (bcolours.OKBLUE + "\n\nIt appears TLS enforcement is in place.  Attempting delivery via bemta\n\n" + bcolours.ENDC)

# find server we are attempting to deliver to
        result = result.splitlines()
        for x in range(2, len(result), 1):
            if 'Sending message using server' in result[x]:
                host = result[x].rsplit(' ')[4]
# generate bemta hostname to use in the same region and az
        bemtahost = "server-1.bemta" + adminbox[adminbox.find('.'):]


# copy local sample to bemta
        scp_copy = subprocess.Popen(["/usr/bin/scp", "-o", "StrictHostKeyChecking=no", location+msgref, bemtahost+":" ],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        scp_copy.wait()

# find and extract the bemta binding ip address to use.  For now we are just going with standard binding for all
        command = sshcmd + bemtahost + ' "' + "sudo cat /opt/msys/ecelerity/etc/ecelerity.conf.d/bindings.d/standard.d/address.conf " + '"'
        output = remote_action(command, sudopw)
        output = output.splitlines()
        for x in range(0, len(output), 1):
            if 'bind_address = ' in output[x]:
                bind = output[x].rsplit(' ')[2]


# swaks copy on remote bemta
        command = sshcmd + bemtahost + ' "' + "cat " + msgref + "| swaks -g -li " + bind + " -f " + sender + " -t " + recipient + " -s " + host + " -tls " + '"'
#       command = delmethod (sshcmd, server,  mx, msgref, recipient)
#        print (command)
        result = remote_action(command, sudopw)
        teststat = printoutput(result, sender, recipient, subject, penid)

# clean up
#    cleanup (msgref, sshcmd, server)
    remove = subprocess.Popen(["rm", location+msgref])
    command = sshcmd + server + ' "' + "rm tmpfile " + msgref + '"'
    remote_action(command, sudopw)


    if (teststat == 'failed'):
        print("No success confirmation.  Examine the output and escalate if necessary")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting")
        remove = subprocess.Popen(["rm", location+msgref])
    except IndexError:
        print("Error.  Invalid email or MX record")
        remove = subprocess.Popen(["rm", location+msgref])
    except Exception as ex:
        print("unexpected Error:")
        print(str(ex))
        remove = subprocess.Popen(["rm", location+msgref])
