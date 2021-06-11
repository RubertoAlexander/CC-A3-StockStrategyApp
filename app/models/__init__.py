import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
s3 = boto3.resource("s3", region_name="us-east-1")

<<<<<<< HEAD
from . import dynamodb_login, dynamodb_register, dynamodb_userdb, s3_register, s3_userBucket, emailapi, tweetapi, config
=======
from . import dynamodb_login, dynamodb_register, dynamodb_userdb, dynamodb_favourites, s3_register
>>>>>>> a92254a3195f9f4f3b877ba8e1918757034e9a53
