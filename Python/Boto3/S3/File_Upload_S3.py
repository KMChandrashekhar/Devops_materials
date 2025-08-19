import boto3

s3 = boto3.client('s3')
bucket_name = 'my-company-logs'
file_path = 'logs/app.log'

s3.upload_file(file_path, bucket_name, 'app/app.log')
