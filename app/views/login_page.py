from flask import render_template, request, redirect

from app import app

@app.route("/login")
def login_page():
    return render_template("loginpage.html")

@app.route("/login", methods = ["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    testing = "username: " + username + " password: " + password

    return testing