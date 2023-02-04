#!/usr/bin/python


import boto3
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if [instance][0][u'State'][u'Name'] == 'running':
                print "tag = ", [instance][0][u'Tags'][0][u'Value'] ,":" ,"private IP" , [instance][0][u'PrivateIpAddress'] ,":" , "running instance"
        elif [instance][0][u'State'][u'Name'] == 'stopped':
                print "tag = ", [instance][0][u'Tags'][0][u'Value'] ,":" ,"private IP" , [instance][0][u'PrivateIpAddress'] ,":" , "stopped instance"
        else:
                print "tag = ", [instance][0][u'Tags'][0][u'Value'] ,":" , "This instance is in terminated state"
