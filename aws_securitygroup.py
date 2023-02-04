#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response = client.describe_security_groups()
for i in  response[u'SecurityGroups']:
        try:

                if [i][0][u'IpPermissions'][0][u'IpRanges'][0][u'CidrIp'] != '0.0.0.0/0':
                        print[i][0][u'GroupId'],":", [i][0][u'IpPermissions'][0][u'IpRanges'][0][u'CidrIp']
                else:
                        print[i][0][u'GroupId'],":", [i][0][u'IpPermissions'][0][u'IpRanges'][0][u'CidrIp']

        except:
                continue
