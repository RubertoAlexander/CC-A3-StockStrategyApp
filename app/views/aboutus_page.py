from flask import render_template, request, redirect

from app import app

@app.route("/aboutus_page")
def aboutus_page():
    return render_template("aboutuspage.html")