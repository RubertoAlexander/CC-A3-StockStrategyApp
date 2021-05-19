from flask import render_template, request, redirect

from app import app

# @app.route("/myuserdetails_page/")
# def myuserdetails_page():
#     username = "Testing"
#     return render_template("myuserpage.html", username = username)

@app.route("/myuserdetails_page/<string:username>")
def myuserdetails_page(username):
    return render_template("myuserpage.html", username = username)


@app.route("/changeaccountdetails_page/<string:username>")
def changeaccountdetails_page(username):
    return render_template("changeaccountdetailspage.html", username = username)