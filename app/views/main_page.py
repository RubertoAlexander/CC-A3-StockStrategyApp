from app.models import dynamodb_favourites
from flask import render_template, request, redirect, make_response

from app import app

@app.route("/")
def main_page():
    username = request.cookies.get("username")
    if not username:
        return redirect("/login")

    favourites = dynamodb_favourites.get_favourites(username)
    print(favourites)
    fav_stocks = []
    for stock in favourites["stocks"]:
        fav_stocks.append(stock[:3])
    print(fav_stocks)
        
    return render_template("mainpage.html", username=username, favs=fav_stocks)

@app.route("/logout")
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("username")
    return response