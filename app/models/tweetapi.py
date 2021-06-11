import requests

from app.models import config

def streamtweets():
    url = "https://api.twitter.com/2/users/28002931/tweets"
    headers = {"Authorization": config.tweetAPI_key()}
    response = requests.get(url, headers = headers)
    tweets = eval(response.text)

    tweet_id_list = []

    for tweet in tweets["data"]:
        tweet_id_list.append(tweet["id"])

    return tweet_id_list