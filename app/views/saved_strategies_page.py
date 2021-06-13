from flask import render_template, request, redirect, jsonify

from app import app
from app.models import dynamodb_strategies

@app.route("/saved", methods=["GET", "POST"])
def saved_strategies():
    username = request.cookies.get("username")
    if not username: return redirect("/login")

    strategies = dynamodb_strategies.get_strategies(username)
    
    return render_template("saved_strategies.html", saved=strategies, username=username)