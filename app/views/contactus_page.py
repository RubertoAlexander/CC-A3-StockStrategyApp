from flask import render_template, request, redirect

from app import app

@app.route("/contact")
def contactus_page():
    return render_template("contactuspage.html")