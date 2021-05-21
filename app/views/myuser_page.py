from flask import render_template, request, redirect

from app import app

# @app.route("/myuserdetails_page/")
# def myuserdetails_page():
#     username = "Testing"
#     return render_template("myuserpage.html", username = username)

@app.route("/myuserdetails_page")
def myuserdetails_page():
    username = request.cookies.get("username")
    if not username: redirect("/login")

    return render_template("myuserpage.html", username = username)


@app.route("/changeaccountdetails_page")
def changeaccountdetails_page():
    username = request.cookies.get("username")
    if not username: redirect("/login")
    
    return render_template("changeaccountdetailspage.html", username = username)