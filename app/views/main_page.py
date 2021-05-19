from flask import render_template, request, redirect

from app import app

@app.route("/")
def main_page():
    username = request.cookies.get("username")
    if not username: redirect("/login")
        
    return render_template("mainpage.html", username=username)