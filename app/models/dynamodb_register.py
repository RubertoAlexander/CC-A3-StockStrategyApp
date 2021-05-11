from . import dynamodb
from botocore.exceptions import ClientError

from boto3.dynamodb.conditions import Attr
table = dynamodb.Table("a3-user")

def checkEmailIfUsed(email) -> str:
    response = table.scan(
        FilterExpression = Attr("email").eq(email)
    )

    items =  response["Items"]

    if(len(items) != 0):
        return "Email already exists. Please try again"
    else:
        return "empty"

def checkUsernameIfUsed(username) -> str:
    response = table.scan(
        FilterExpression = Attr("username").eq(username)
    )

    items =  response["Items"]

    if(len(items) != 0):
        return "Username already exists. Please try again"
    else:
        return "empty"

def addUser(email, username, password):
    table.put_item(
        Item = {
            "email": email,
            "username": username,
            "password": password
        }
    )