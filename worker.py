import boto3
from botocore.client import Config

s3 = boto3.client("s3", config=Config(signature_version="s3v4"))
sns = boto3.client("sns")

def process_event(event):
    sns.publish(TopicArn="arn:aws:sns:eu-west-1:123456789:alerts", Message=str(event))
