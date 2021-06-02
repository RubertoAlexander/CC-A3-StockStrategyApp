from . import dynamodb
from botocore.exceptions import ClientError

from boto3.dynamodb.conditions import Attr
table = dynamodb.Table("a3-user")

def authenticateUser(username, password) -> str:
    response = table.scan(
        FilterExpression = Attr("username").eq(username) & Attr("password").eq(password)
    )

    items = response["Items"]

    if(len(items) == 0):
        return None
    else:
        return items[0]