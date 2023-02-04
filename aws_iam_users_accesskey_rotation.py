#!/usr/bin/python

import datetime
from datetime import datetime
import boto3

client = boto3.client('iam')
response = client.list_users() ##describing iam for getting all the usernames.
for x in range(len(response[u'Users'])):
    users = (response[u'Users'][x][u'UserName'])  
    response01 = client.list_access_keys(UserName=users)
    if response01[u'AccessKeyMetadata']!=[]:
        status=(response01[u'AccessKeyMetadata'][0][u'Status'])
        create_date=(response01[u'AccessKeyMetadata'][0][u'CreateDate'])
        c_date=str(create_date)
        acc_key_id=(response01[u'AccessKeyMetadata'][0][u'AccessKeyId'])
        val= datetime.strptime(c_date, '%Y-%m-%d %H:%M:%S+00:00')
        date=str(datetime.now())
        now=datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f')
        if ((now-val).days) >=60:        ##applying condition like if the age of access keys are >=60 days, it will create new access key pairs
                user='demo'              ##here i directly passed one user, you can get the list of usenames thorugh "describing iam"
response02 =client.create_access_key(UserName=user)
u_name=(response02[u'AccessKey'][u'UserName'])
acc_id=(response02[u'AccessKey'][u'AccessKeyId'])
sec_id=(response02[u'AccessKey'][u'SecretAccessKey'])
stat=(response02[u'AccessKey'][u'Status'])
output=u_name,acc_id,sec_id,stat
print(output)





##this is a python 2.x code and the modules I imported here is python 2.x module.If you are using python 3.x ,make sure you imported the corret module
