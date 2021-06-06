from app.models import dynamodb_favourites
from flask import render_template, request, redirect, make_response

from app import app

@app.route("/")
def main_page():
    username = request.cookies.get("username")
    # if not username:
    #     return redirect("/login")
        
    return render_template("mainpage.html", username=username)

@app.route("/logout")
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("username")
    return response