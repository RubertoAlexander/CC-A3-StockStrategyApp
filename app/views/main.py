from flask import render_template, request, redirect

from app import app

@app.route("/")
def helloworld():
    return render_template("helloworld.html")