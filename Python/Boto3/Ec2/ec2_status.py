
####################################################################################################################################################
## LIST ALL INSTANCES
import boto3
ec2 = boto3.resource('ec2',region_name='ap-south-1')
for instance in ec2.instances.all():
     print(
         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\nTag: {6}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state, instance.tags
         )
     )

####################################################################################################################################################
## FILTER Instances only running, stopped, etc
'''
import boto3
ec2 = boto3.resource('ec2')
inst = ec2.instances.filter(

Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in inst:
     print(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state 
     )
else:
     print('No running instance')
'''
####################################################################################################################################################
## DESCRIBE Particular Intance 
'''
import boto3
ec2 = boto3.client('ec2')
responce = ec2.describe_instance_status(
    InstanceIds=[
        'i-039d442e843ef6c2f',
    ],
)
print(responce)
'''