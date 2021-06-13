from app.models import dynamodb_favourites
from flask import render_template, request, redirect, make_response

from app import app

from app.models import tweetapi

@app.route("/")
def splash():
    username = request.cookies.get("username")
        
    return render_template("splash.html", username = username)