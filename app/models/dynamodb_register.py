from . import dynamodb
from botocore.exceptions import ClientError

from boto3.dynamodb.conditions import Attr

from app.models import dynamodb_userdb

table = dynamodb.Table("a3-user")

def checkRetypePassword(password, retype_password) -> bool:
    result = False
    
    if(password == retype_password):
        result = True

    return result

def checkEmailIfUsed(email) -> str:
    items = dynamodb_userdb.checkEmailInDB(email)

    if(len(items) != 0):
        return "Email already exists. Please try again"
    else:
        return "empty"

def checkUsernameIfUsed(username) -> str:
    items = dynamodb_userdb.checkUsernameInDB(username)

    if(len(items) != 0):
        return "Username already exists. Please try again"
    else:
        return "empty"

def addUser(email, username, password):
    image_version = "1"

    table.put_item(
        Item = {
            "email": email,
            "username": username,
            "password": password,
            "image_version": image_version
        }
    )