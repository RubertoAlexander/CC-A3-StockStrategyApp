from flask import render_template, request, redirect, jsonify

from app import app
from app.models import dynamodb_favourites, yf_stock

@app.route("/stock/<symbol>", methods=["GET"])
def stock_page(symbol: str):
    username = request.cookies.get("username")
    if not username: return redirect("/login")

    stock = {
        "symbol": symbol,
        "name": yf_stock.get_name(symbol),
        "prices": yf_stock.get_prices(symbol)
    }

    favourites = dynamodb_favourites.get_favourites(username)
    
    return render_template("stock_page.html", stock=stock, favs=favourites["stocks"])

@app.route("/fav/<symbol>", methods=["POST"])
def favourite(symbol: str):
    username = request.cookies.get("username")
    favourites = dynamodb_favourites.get_favourites(username)
    stocks = favourites["stocks"]

    if symbol in stocks:
        stocks.remove(symbol)
        added = False
    else:
        stocks.append(symbol)
        added = True

    result = dynamodb_favourites.put_favourites(username, stocks)
    if result:
        fav_dict = jsonify(
            added=added,
            favs=stocks
        )
        return fav_dict