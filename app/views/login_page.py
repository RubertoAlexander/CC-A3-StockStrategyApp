from flask import render_template, request, redirect, url_for

from app import app

from app.models import dynamodb_login

@app.route("/login_page")
def login_page():
    return render_template("loginpage.html")

@app.route("/login", methods = ["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = dynamodb_login.authenticateUser(username, password)

    # if user failed authentication
    if(user == None):
        return render_template("loginpage.html", loginError = "Incorrect details. Please try again.")

    # admin webpage
    elif(user["username"] == "admin"):
        return redirect(url_for("admin_page", username = user["username"]))

    # user webpage
    else:        
        return render_template("mainpage.html", username = username)