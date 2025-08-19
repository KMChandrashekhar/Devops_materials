import boto3
client = boto3.resource('ec2') 
Tags = {'Name': 'tag:Name', 'Values': ['Jenkins1']}
instance_type = {'Name': 'instance-type', 'Values': ['t2.micro']}

for instance in client.instances.filter(Filters=[Tags]): ## Change filter Tags or instance_type
  #print(f"Instance ID: {instance.id}")
    instance.start() #To stop instance
    instance.stop()  #To start instance
    print('Instance stopped')
