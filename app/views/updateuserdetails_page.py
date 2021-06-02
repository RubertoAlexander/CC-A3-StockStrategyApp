from flask import render_template, request, redirect

from app import app

from app.models import dynamodb_userdb


@app.route("/updateuserdetail_page")
def updateuserdetail_page():
    username = request.cookies.get("username")
    
    user = dynamodb_userdb.getUserFromUsername(username)
    return render_template("updateuserdetailpage.html", username = username, user = user)

@app.route("/updatedetails", methods = ["POST"])
def updatedetails():
    username = request.cookies.get("username")

    new_email = request.form["email"]
    new_username = request.form["username"]

    new_image = request.files["file"]

    if new_image == None:
        return "True"
    else:
        return "False"

def isNewEmailValid(email) -> bool:
    email_items = dynamodb_userdb.checkEmailInDB(email)

    if(len(email_items) == 0):
        return True
    else:
        return False       

def isNewUsernameValid(username) -> bool:
    username_items = dynamodb_userdb.checkUsernameInDB(username)

    if(len(username_items) == 0):
        return True
    else:
        return False   