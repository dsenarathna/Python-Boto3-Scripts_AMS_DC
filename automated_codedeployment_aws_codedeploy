import boto3
client = boto3.client('codedeploy')
def lambda_handler(event,context):
    response = client.create_deployment(applicationName='your-app-name',deploymentGroupName='your-deployment-group-name',revision={'revisionType': 'S3','s3Location': {'bucket': 'bucket-name','key':'yourfile.zip','bundleType': 'zip'}},
    deploymentConfigName='CodeDeployDefault.OneAtATime',
    ignoreApplicationStopFailures=False,
    targetInstances={
        'tagFilters': [
            {
                'Key': 'Name',  ##key of your ec2 instance
                'Value': 'ah-app', ##Value of your ec2 instance
                'Type': 'KEY_AND_VALUE'
            },
        ],
    }, 
    autoRollbackConfiguration={'enabled': True,'events': ['DEPLOYMENT_FAILURE']})
