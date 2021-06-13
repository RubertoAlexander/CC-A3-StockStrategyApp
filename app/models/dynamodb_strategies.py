from . import dynamodb
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

TABLE = dynamodb.Table('strategy')

def get_strategies(username: str) -> dict:
    response = TABLE.query(
        KeyConditionExpression=Key('username').eq(username)
    )

    return response['Items']

def put_strategy(username: str, strategy: str, params: dict) -> bool:
    
    item = {
        'username': username,
        'strategy_name': strategy,
        'params': params
    }

    try:
        TABLE.put_item(Item=item)
    except ClientError:
        return False
    else:
        return True