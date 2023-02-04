import boto3
client = boto3.client('cloudwatch')
def lambda_handler(event, context):  
    id=event[u'detail'][u'EC2InstanceId']
    ##id is a variable having instance id in it.
    response = client.delete_alarms(
    AlarmNames=['CPU_Utilization' + id,'DiskSpace' + id,'MemoryUtilization' + id] ##deleting the cloudwatch alarms having name like "'CPU_Utilization id-******,'DiskSpace id-*******,'MemoryUtilization idd-*******' + id"
    )
    
