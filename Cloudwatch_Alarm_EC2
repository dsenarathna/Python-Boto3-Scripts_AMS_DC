import boto3
#importing time module
import time

print("Function is sleeeping for 5 minutes")
time.sleep(180)
print("Function Loaded")

cloudwatch = boto3.client('cloudwatch')
client = boto3.client('cloudwatch')
ec2client = boto3.client('ec2')
def lambda_handler(event, context):
    id=event[u'detail'][u'EC2InstanceId']
    ##id is a variable which will store  ec2 instance id
    response = client.list_metrics(
    Namespace='System/Linux',
    MetricName='DiskSpaceUtilization',
    Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': id
            },
        ],
    )
    Filesys=response[u'Metrics'][0][u'Dimensions'][2][u'Value']
    ##Filesys is a variable which will store file system of the EC2 disk
    cloudwatch.put_metric_alarm(
    AlarmName='CPU_Utilization' + id,
    AlarmActions=[ 'arn:aws:sns:******************',],
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=5,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=80.0,
    ActionsEnabled=True,
    AlarmDescription='Alarm when server CPU exceeds 80%',
    Dimensions=[
            {
    'Name': 'InstanceId',
    'Value': id
            },
    ]
    )
    cloudwatch.put_metric_alarm(
    AlarmName='DiskSpace' + id,
    AlarmActions=[ 'arn:aws:sns:**********************'],
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=5,
    MetricName='DiskSpaceUtilization',
    Namespace='System/Linux',
    Period=60,
    Statistic='Average',
    Threshold=90.0,
    ActionsEnabled=True,
    AlarmDescription='Alarm when server DISK exceeds 90%',
    Dimensions=[
        {
    "Name": "Filesystem",
    "Value": Filesys
        },
        {
    'Name': 'InstanceId',
    'Value': id
        },
        {
    "Name": "MountPath",
    "Value": "/"
        }
    ],
    )
    cloudwatch.put_metric_alarm(
    AlarmName='MemoryUtilization' + id,
    AlarmActions=[ 'arn:aws:sns:****************************'],
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=5,
    MetricName='MemoryUtilization',
    Namespace='System/Linux',
    Period=60,
    Statistic='Average',
    Threshold=90.0,
    ActionsEnabled=True,
    AlarmDescription='Alarm when server MEMORY exceeds 90%',
    Dimensions=[
        {
    'Name': 'InstanceId',
    'Value': id
        },
    ],
    )


