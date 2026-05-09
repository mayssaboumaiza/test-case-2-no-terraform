import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")
sqs = boto3.client("sqs", region_name="eu-west-1")
dynamodb = boto3.resource("dynamodb")

def upload_file(bucket, key, body):
    s3.put_object(Bucket=bucket, Key=key, Body=body)

def send_message(queue_url, message):
    sqs.send_message(QueueUrl=queue_url, MessageBody=message)
