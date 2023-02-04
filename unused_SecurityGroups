#!/usr/bin/python
import boto3
import re
client = boto3.client('ec2')
ec2 = boto3.client('ec2')
my_session = boto3.session.Session()
my_region = my_session.region_name

list1 = []
list2 = []
list3 = []
list4 = []

ec2 = boto3.resource('ec2') #You have to change this line based on how you pass AWS credentials and AWS config
sgs = list(ec2.security_groups.all())
#print sgs

response = client.describe_security_groups()
for i in response[u'SecurityGroups']:
        groupID = (i[u'GroupId'])
        list1.append(groupID)
#print list1
insts = list(ec2.instances.all())

all_sgs = set(list1)
all_inst_sgs = set([sg[u'GroupId'] for inst in insts for sg in inst.security_groups])
unused_sgs = all_sgs - all_inst_sgs
print " EC2 used SecurityGroup: ",list(all_inst_sgs)
print " EC2 unused SecurityGroup: ",list(unused_sgs)
ec2 = boto3.client('ec2')
#region_list = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
#print region_list
#for region in region_list:
elb_client = boto3.client('elbv2', region_name=my_region)
elbs = elb_client.describe_load_balancers()
for elb in elbs['LoadBalancers']:
#val = (elb[u'SecurityGroups']),(elb[u'LoadBalancerName'])
		val2 = elb[u'SecurityGroups']
		list2.append(val2)
for x in list2:
        for y in x:
                list3.append(y)

elb_sgs = set(list3)
#print elb_sgs
unused_sgs_elb = all_sgs - elb_sgs
print " ELB used SecurityGroup: ",list3
print " ELB unused SecurityGroup: ",list(unused_sgs_elb)
client = boto3.client('rds')
response = client.describe_db_instances()
#print response
for rds in response['DBInstances']:
        var1 = rds[u'VpcSecurityGroups'][0][ u'VpcSecurityGroupId']
        list4.append(var1)
#print list4

rds_sgs = set(list4)

unused_sgs_rds = all_sgs - rds_sgs
print " RDS used SecurityGroup: ",list4
print " RDS unused SecurityGroup: ",list(unused_sgs_rds)
