#Boto3 code for uploading a file to an S3 bucket
#In my code bucket name is pbx-httpd-logs and file name is httpd.log available in the same directory.
import boto3
s3 = boto3.client('s3')
bucket_name = 'pbx-httpd-logs'
file_path = 'httpd.log'
API_KEY = 'hfkbddhededmekdhe'
s3.upload_file(file_path, bucket_name, 'httpd')
print(f"File {file_path} uploaded to bucket {bucket_name} as 'httpd'")  # Confirmation message


