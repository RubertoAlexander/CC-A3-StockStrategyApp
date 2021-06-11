from flask import render_template, request, redirect, url_for, make_response

from app import app

from app.models import dynamodb_register, s3_register

@app.route("/register_page")
def register_page():
    return render_template("registerpage.html")

@app.route("/register", methods = ["POST"])
def register():
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    retype_password = request.form["retype_password"]

    # Checking if both passwords match
    check_retype_password = dynamodb_register.checkRetypePassword(password, retype_password)
    if not (check_retype_password):
        return render_template("registerpage.html", registerError = "Passwords do not match. Please re-enter again.")

    # Checking if username is taken
    check_username = dynamodb_register.checkEmailIfUsed(username)
    if not (check_username == "empty"):
        return render_template("registerpage.html", registerError = check_username)
    
    # Checking if email is taken
    check_email = dynamodb_register.checkEmailIfUsed(email)
    if not (check_email == "empty"):
        return render_template("registerpage.html", registerError = check_email)

    ## IF all good,
    # Add user image to s3
    imagefile = request.files["file"]

    s3_register.addUserImage(username, imagefile)

    # Add user to dynamodb database
    dynamodb_register.addUser(email, username, password)

    # Instead of redirecting user back to main page and not logged in,
    # why not direct user to main page while logged in?
    
    # # Return to main page and not logged in
    # return redirect(url_for("main_page"))

    # Return to main page and logged in
    response = make_response(redirect("/"))
    response.set_cookie("username", username)      
    return response