from flask import render_template, request, redirect, jsonify

from app import app
from app.models import dynamodb_favourites, dynamodb_strategies

@app.route("/builder", methods=["GET", "POST"])
def builder_strategy_page():
    username = request.cookies.get("username")
    if not username: return redirect("/login")

    favourites = dynamodb_favourites.get_favourites(username)
    
    return render_template("builder_strategy.html", favs=favourites["stocks"], username=username)

@app.route("/builder/<name>")
def builder_display(name: str):
    username = request.cookies.get("username")
    if not username: return redirect("/login")

    favourites = dynamodb_favourites.get_favourites(username)
    strategies = dynamodb_strategies.get_strategies(username)
    selected = None
    for strategy in strategies:
        if strategy["strategy_name"] == name:
            selected = strategy
    
    return render_template("builder_strategy.html", favs=favourites["stocks"], username=username, selected=selected)


@app.route("/builder/<stock>/save/<name>", methods=["POST"])
def save_strategy(stock: str, name: str):
    username = request.cookies.get("username")

    timerange = request.json["timerange"]
    interval = request.json["interval"]
    buy_rules = request.json["indicator_buys"]
    sell_rules = request.json["indicator_sells"]

    params = {
        "stock": stock,
        "timerange": timerange,
        "interval": interval,
        "buy_rules": buy_rules,
        "sell_rules": sell_rules 
    }

    result = dynamodb_strategies.put_strategy(username, name, params)
    print(result)

    return jsonify(result)
    