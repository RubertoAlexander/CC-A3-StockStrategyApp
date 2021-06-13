from app.models import dynamodb_favourites
from flask import render_template, request, redirect, make_response

from app import app

from app.models import tweetapi, newsapi

@app.route("/home")
def main_page():
    username = request.cookies.get("username")
    if not username: redirect("/login")
    
    # news_list = newsapi.getNews()
    # tweet_id_list = tweetapi.streamtweets()

    news_list = []
    tweet_id_list = []
        
    return render_template("mainpage.html", username = username, tweet_id_list = tweet_id_list, news_list = news_list)

@app.route("/logout")
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("username")
    return response