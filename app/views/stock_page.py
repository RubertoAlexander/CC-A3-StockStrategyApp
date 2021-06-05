from flask import render_template, request, redirect

from app import app

@app.route("/stock")
def stock_page():
    username = request.cookies.get("username")
    if not username: redirect("/login")
        
    return render_template("stock_page.html")