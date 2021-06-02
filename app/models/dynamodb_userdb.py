from . import dynamodb
from botocore.exceptions import ClientError

from boto3.dynamodb.conditions import Attr
table = dynamodb.Table("a3-user")

def getUserFromUsername(username):
    response = table.scan(
        FilterExpression = Attr("username").eq(username)
    )

    items = response["Items"]

    if(len(items) == 0):
        return None
    else:
        return items[0]

def checkEmailInDB(email):
    response = table.scan(
        FilterExpression = Attr("email").eq(email)
    )

    items =  response["Items"]

    return items

    
def checkUsernameInDB(username):
    response = table.scan(
        FilterExpression = Attr("username").eq(username)
    )

    items =  response["Items"]

    return items