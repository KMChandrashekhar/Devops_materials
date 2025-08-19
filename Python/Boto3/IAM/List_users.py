import boto3

aws_console = boto3.session.Session(profile_name="boto3")
# Create IAM client

iam = aws_console.resource('iam')
for each_user in iam.users.all():
    print(each_user)
