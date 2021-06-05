from flask import render_template, request, redirect

from app import app
from app.models import yf_stock

@app.route("/stock/<symbol>")
def stock_page(symbol: str):
    username = request.cookies.get("username")
    if not username: redirect("/login")

    stock = {
        "symbol": symbol,
        "name": yf_stock.get_name(symbol),
        "prices": yf_stock.get_prices(symbol)
    }
        
    return render_template("stock_page.html", stock=stock)