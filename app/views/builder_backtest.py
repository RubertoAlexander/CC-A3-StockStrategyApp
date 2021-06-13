from flask import render_template, request, redirect, jsonify

from app import app
from app.models import backtest, dynamodb_favourites, yf_stock

@app.route("/builder/backtest/<stock>", methods=["GET", "POST"])
def builder_backtest_page(stock: str):
    username = request.cookies.get("username")
    if not username: return redirect("/login")

    timerange = request.json["timerange"]
    interval = request.json["interval"]
    buy_rules = request.json["indicator_buys"]
    sell_rules = request.json["indicator_sells"]

    print(stock, timerange, interval, buy_rules, sell_rules)

    data = yf_stock.get_data(interval, stock, timerange)

    result = backtest.run(data, buy_rules, sell_rules)
    
    return jsonify({
        "profit": result["profit"], 
        "trades": result["trades"],
        "win": result["win"],
        "lose": result["lose"]
        })