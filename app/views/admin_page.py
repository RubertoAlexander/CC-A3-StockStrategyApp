from flask import render_template, request, redirect

from app import app

@app.route("/admin_page/<string:username>")
def admin_page(username):
    return render_template("adminmainpage.html", username = username)

@app.route("/admindisplayusers_page/<string:username>")
def admindisplayusers_page(username):
    return "Placeholder - To be done"