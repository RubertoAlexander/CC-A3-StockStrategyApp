import requests
from requests.models import Response

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

REGION = "AU"   

headers = {
    'x-rapidapi-key': "fd38072801msh94e42590875e834p1d8df6jsnc07d0376b458",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

def search(query: str):
    querystring = {"q":query, "region":REGION}

    response = get_response(querystring)
    return response

def get_response(query: dict) -> Response:
    response = requests.request("GET", url, headers=headers, params=query)
    return response.json()