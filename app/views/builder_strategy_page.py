from flask import render_template, request, redirect, jsonify

from app import app
from app.models import dynamodb_favourites

@app.route("/builder", methods=["GET", "POST"])
def builder_strategy_page():
    username = request.cookies.get("username")
    if not username: return redirect("/login")

    favourites = dynamodb_favourites.get_favourites(username)
    print(favourites)
    
    return render_template("builder_strategy.html", favs=favourites["stocks"])

@app.route("/builder/<stock>/save/<name>", methods=["POST"])
def save_strategy(stock: str, name: str):
    username = request.cookies.get("username")

    timerange = request.json["timerange"]
    interval = request.json["interval"]
    buy_rules = request.json["indicator_buys"]
    sell_rules = request.json["indicator_sells"]

    print("saved")
    