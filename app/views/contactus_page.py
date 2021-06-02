from flask import render_template, request, redirect

from app import app

@app.route("/contactus_page")
def contactus_page():
    username = request.cookies.get("username")

    return render_template("contactuspage.html", username=username)