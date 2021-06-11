from app.models import dynamodb_favourites
from flask import render_template, request, redirect, make_response

from app import app

from app.models import tweetapi



# curl --request GET "https://api.twitter.com/2/users/28002931/tweets" --header "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAAO%2BQQEAAAAAr5ZOz5kSTKd0%2BX%2Bdme2pvGQGiy0%3DvjMZpdprox8EQSAZiDQlw0Qmm7pM8naocwG9jGg4R34nyjtaxz"

@app.route("/")
def main_page():
    username = request.cookies.get("username")
    if not username: redirect("/login")
    
    tweet_id_list = tweetapi.streamtweets()
        
    return render_template("mainpage.html", username = username, tweet_id_list = tweet_id_list)

@app.route("/logout")
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("username")
    return response