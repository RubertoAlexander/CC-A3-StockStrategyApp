from flask import render_template, request, redirect

from app import app

@app.route("/admin")
def admin_page():
    username = request.cookies.get("username")
    if not username: return redirect("/login")
    
    return render_template("adminmainpage.html", username = username)

@app.route("/admindisplayusers")
def admindisplayusers_page():
    return "Placeholder - To be done"