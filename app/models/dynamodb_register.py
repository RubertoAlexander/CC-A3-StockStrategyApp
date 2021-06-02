from . import dynamodb
from botocore.exceptions import ClientError

from boto3.dynamodb.conditions import Attr

from app.models import dynamodb_userdb

table = dynamodb.Table("a3-user")

def checkEmailIfUsed(email) -> str:
    # response = table.scan(
    #     FilterExpression = Attr("email").eq(email)
    # )

    # items =  response["Items"]

    items = dynamodb_userdb.checkEmailInDB(email)

    if(len(items) != 0):
        return "Email already exists. Please try again"
    else:
        return "empty"

def checkUsernameIfUsed(username) -> str:
    # response = table.scan(
    #     FilterExpression = Attr("username").eq(username)
    # )

    # items =  response["Items"]

    items = dynamodb_userdb.checkUsernameInDB(username)

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