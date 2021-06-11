from flask import render_template, request

from app import app

from app.models import dynamodb_register, dynamodb_userdb

@app.route("/updatepassword_page")
def updatepassword_page():
    username = request.cookies.get("username")
    
    return render_template("updateuserpassword.html", username = username)

@app.route("/updatepassword", methods = ["POST"])
def updatepassword():
    username = request.cookies.get("username")

    old_password = request.form["old_password"]
    new_password = request.form["new_password"]
    retype_password = request.form["retype_password"]

    # Verify Old Password
    curr_password = dynamodb_userdb.getPasswordFromUsername(username)
    if(curr_password != old_password):
        return render_template("updateuserpassword.html", username = username,
                            updateMessage = "Incorrect Old Password. Please re-enter again.")

    # Checking if both passwords match
    check_retype_password = dynamodb_register.checkRetypePassword(new_password, retype_password)
    if not (check_retype_password):
        return render_template("updateuserpassword.html", username = username,
                                 updateMessage = "New Passwords do not match. Please re-enter again.")

    dynamodb_userdb.updateUserPassword(username, new_password)

    return render_template("itisupdated_userdetailpage.html", username = username)