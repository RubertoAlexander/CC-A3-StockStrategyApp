from flask import render_template, request, redirect, url_for, make_response

from app import app

from app.models import dynamodb_login

@app.route("/login")
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
        response = make_response(redirect("/admin"))
        response.set_cookie("username", user["username"])
        return response

    # user webpage
    else:
        response = make_response(redirect("/"))
        response.set_cookie("username", user["username"])      
        return response