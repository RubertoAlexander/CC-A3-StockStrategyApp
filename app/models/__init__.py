import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
s3 = boto3.resource("s3", region_name="us-east-1")

from . import dynamodb_login, dynamodb_register, s3_register