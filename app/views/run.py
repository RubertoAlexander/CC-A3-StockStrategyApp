from flask import render_template, request, redirect, url_for

from app import app

@app.route("/")
def index():
    return redirect("/main_page")
    
@app.route("/placeholderfunction")
def placeholderfunction():
    return "Placeholder - It works!"