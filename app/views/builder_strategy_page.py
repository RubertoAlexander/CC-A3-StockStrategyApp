from flask import render_template, request, redirect, jsonify

from app import app
from app.models import dynamodb_favourites, yf_stock

@app.route("/builder/strategy", methods=["GET", "POST"])
def builder_strategy_page():
    username = request.cookies.get("username")
    if not username: return redirect("/login")

    favourites = dynamodb_favourites.get_favourites(username)
    print(favourites)
    
    return render_template("builder_strategy.html", favs=favourites["stocks"], username=username)