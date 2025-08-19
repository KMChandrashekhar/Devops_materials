##Provide Name properly under Values section Example: 'Values': ['Jenkins']
## Make sure you have the necessary permissions to start/stop instances in your AWS account.

import boto3
client = boto3.resource('ec2') 
Tags = {'Name': 'tag:Name', 'Values': ['Jenkins']}
instance_type = {'Name': 'instance-type', 'Values': ['t2.micro']}

for instance in client.instances.filter(Filters=[Tags]): ## Change filter Tags or instance_type
  #print(f"Instance ID: {instance.id}")
    #instance.start() #To stop instance
    instance.stop()  #To start instance
    #print('Instance started')
    print('Instance Stopped')

#Note: Make sure comment/uncomment the start/stop line as per your requirement.