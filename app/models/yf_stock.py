import requests
from requests.models import Response

from app.models import config

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2"

REGION = "AU"

headers = {
    'x-rapidapi-key': config.stockAPI_key(),
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

def get_name(symbol: str):
    response = get_summary(symbol)
    return response["quoteType"]["longName"]

def get_prices(symbol: str):
    response = get_summary(symbol)
    prices = {
        "price": response["price"]["regularMarketPrice"]["raw"],
        "open": response["price"]["regularMarketOpen"]["raw"],
        "high": response["price"]["regularMarketDayHigh"]["raw"],
        "low": response["price"]["regularMarketDayLow"]["raw"],
        "close": response["price"]["regularMarketPreviousClose"]["raw"],
    }
    return prices

def get_summary(symbol: str):
    endpoint = url + "/get-summary"
    querystring = {"symbol":symbol, "region":REGION}

    response = get_response(querystring, endpoint)
    return response

def get_response(query: dict, endpoint: str) -> Response:
    response = requests.request("GET", endpoint, headers=headers, params=query)
    return response.json()