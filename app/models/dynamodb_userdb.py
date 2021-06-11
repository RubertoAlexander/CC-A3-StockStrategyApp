from typing import ItemsView
from . import dynamodb
from botocore.exceptions import ClientError

from boto3.dynamodb.conditions import Attr

table = dynamodb.Table("a3-user")

def getAllUsers():
    response = table.scan()

    items = response["Items"]

    return items

def getUserFromUsername(username):
    response = table.scan(
        FilterExpression = Attr("username").eq(username)
    )

    items = response["Items"]

    if(len(items) == 0):
        return None
    else:
        return items[0]

def getEmailFromUsername(username):
    response = table.scan(
        FilterExpression = Attr("username").eq(username)
    )

    items = response["Items"]

    if(len(items) == 0):
        return None
    else:
        return items[0]["email"]

def getImageVersionFromUsername(username):
    response = table.scan(
        FilterExpression = Attr("username").eq(username)
    )

    items = response["Items"]

    if(len(items) == 0):
        return None
    else:
        return items[0]["image_version"]

def getPasswordFromUsername(username):
    response = table.scan(
        FilterExpression = Attr("username").eq(username)
    )

    items = response["Items"]

    if(len(items) == 0):
        return None
    else:
        return items[0]["password"]

def checkEmailInDB(email):
    response = table.scan(
        FilterExpression = Attr("email").eq(email)
    )

    items =  response["Items"]

    return items

def isNewEmailValid(email) -> bool:
    email_items = checkEmailInDB(email)

    if(len(email_items) == 0):
        return True
    else:
        return False

def updateUserEmail(username, new_email):
    table.update_item(
        Key = {
            "username": username,
        },
        UpdateExpression = "SET email = :new_email",
        ExpressionAttributeValues = {
            ":new_email": new_email
        }
    )

def updateUserImageVersion(username, new_image_version):
    table.update_item(
        Key = {
            "username": username,
        },
        UpdateExpression = "SET image_version = :new_image_version",
        ExpressionAttributeValues = {
            ":new_image_version": new_image_version
        }
    )

def updateUserPassword(username, new_password):
    table.update_item(
        Key = {
            "username": username,
        },
        UpdateExpression = "SET password = :new_password",
        ExpressionAttributeValues = {
            ":new_password": new_password
        }
    )

def deleteUserFromUserDB(username):
    table.delete_item(
        Key = {
            "username": username
        }
    )