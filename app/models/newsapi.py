import requests

from app.models import config

def getNews():

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-newsfeed"

    querystring = {"category":"generalnews","region":"AU"}

    headers = {
        'x-rapidapi-key': config.newsAPI_key(),
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

    response =  requests.request("GET", url, headers=headers, params=querystring)

    news_json = response.json()

    news_list = []

    for news in news_json["items"]["result"]:
        news_details = []

        title = news["title"]
        summary = news["summary"]
        author = news["author"]
        url_link = news["link"]

        if(author == ""):
            author = "News"
        
        news_details.append(title)
        news_details.append(summary)
        news_details.append(author)
        news_details.append(url_link)

        news_list.append(news_details)

    return news_list