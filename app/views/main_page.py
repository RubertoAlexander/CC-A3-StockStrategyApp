from flask import render_template, request, redirect

from app import app

@app.route("/")
def main_page():
    return render_template("mainpage.html")