import requests
from requests.models import Response

from app.models import config

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

REGION = "AU"   

headers = {
    'x-rapidapi-key': config.stockAPI_key(),
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

def search(query: str):
    querystring = {"q":query, "region":REGION}

    response = get_response(querystring)
    return response

def get_response(query: dict) -> Response:
    response = requests.request("GET", url, headers=headers, params=query)
    return response.json()