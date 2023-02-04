#!/usr/bin/python

import boto3
client = boto3.client('ec2')
list1 = []
list2 = []


#response = client.describe_volumes()
response = client.describe_vpcs()
response1 = client.describe_flow_logs()
#print response1


for VIds in response[u'Vpcs']:
        vpc = VIds[u'VpcId']
        #print " all VPCIds: ",VIds[u'VpcId']
        list1.append(vpc)
VPCIds = set(list1)
#print " all VPCIds: ", VPCIds


for i in response1[u'FlowLogs']:
        #print " FlowLog VPCIds: ", i[u'ResourceId']
        FLVIds = i[u'ResourceId']
        list2.append(FLVIds)
FlowlogVPCIds = set(list2)
#print " all Flowlogs VPCIds : ", FlowlogVPCIds


VPC_without_FlowLogs = VPCIds - FlowlogVPCIds
#print VPC_without_FlowLogs

val1 = list(VPC_without_FlowLogs)
#val2 = len(VPC_without_FlowLogs)
va2 = list(VPCIds)
#print val
for y in val1:
        response = client.create_flow_logs(

                ClientToken='NewFlowLog',
                DeliverLogsPermissionArn='arn:aws:iam::xxxxxxxxxxxxxxxxxxx:role/cloudwatchagent',
                LogGroupName='FlowlogGroup',
                ResourceIds=[
                        y,
                ],
                ResourceType='VPC',
                TrafficType='ALL',
                LogDestinationType='cloud-watch-logs',
        )
#print response
