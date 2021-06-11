from flask import render_template, request

from app import app

from app.models import emailapi

@app.route("/contactus_page")
def contactus_page():
    username = request.cookies.get("username")

    return render_template("contactuspage.html", username = username)

@app.route("/contactus_sendmessage", methods = ["POST"])
def contactus_sendmessage():
    username = request.cookies.get("username")

    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]
    
    emailapi.sendEmail(name, email, subject, message)

    return render_template("contactuspage.html", username = username, message = "Your message has been sent")