from flask import render_template, request, redirect

from app import app
from app.models import dynamodb_favourites, yf_stock

@app.route("/stock/<symbol>")
def stock_page(symbol: str):
    username = request.cookies.get("username")
    if not username: return redirect("/login")

    stock = {
        "symbol": symbol,
        "name": yf_stock.get_name(symbol),
        "prices": yf_stock.get_prices(symbol)
    }
        
    return render_template("stock_page.html", stock=stock)

@app.route("/fav/<symbol>")
def add_favourite(symbol: str):
    username = request.cookies.get("username")
    favourites = dynamodb_favourites.get_favourites(username)
    stocks = favourites["stocks"]
    stocks.add(symbol+".AX")

    result = dynamodb_favourites.put_favourites(username, stocks)
    return redirect("/stock/"+symbol)