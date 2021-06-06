from . import dynamodb
from botocore.exceptions import ClientError

TABLE = dynamodb.Table('stock-favourites')

def get_favourites(username: str) -> dict:
    user_key = {
        'username' : username
    }
    response = TABLE.get_item(Key=user_key)

    favs = None
    if "Item" in response:
        favs = response['Item']
    
    return favs

def put_favourites(username: str, favs: set) -> bool:

    item = {
        'username': username,
        'stocks': favs
    }

    try:
        TABLE.put_item(Item=item)
    except ClientError:
        return False
    else:
        return True