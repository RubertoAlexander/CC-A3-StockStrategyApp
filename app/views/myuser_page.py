from flask import render_template, request, redirect

from app import app

from app.models import dynamodb_userdb

@app.route("/myuserdetails_page")
def myuserdetails_page():
    username = request.cookies.get("username")

    # Check for admin username
    if username == "admin":
        return render_template("adminuserpage.html", username = username)
    else:
        return render_template("myuserpage.html", username = username)