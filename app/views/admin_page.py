from flask import render_template, request, redirect, url_for

from app import app

from app.models import dynamodb_userdb, s3_userBucket

@app.route("/admin")
def admin_page():
    username = request.cookies.get("username")
    if not username: return redirect("/login")
    
    return render_template("adminuserpage.html", username = username)

@app.route("/admindisplayusers_page")
def admindisplayusers_page():
    username = request.cookies.get("username")
    users = dynamodb_userdb.getAllUsers()
    
    return render_template("admindisplayalluserspage.html", username = username, users = users)

@app.route("/admindisplay_chosenuser", methods = ["POST"])
def admindisplay_chosenuser():
    username = request.cookies.get("username")
    
    # Get the edited user
    editing_username = request.form["username"]
    editing_user = dynamodb_userdb.getUserFromUsername(editing_username)

    return render_template("adminedituserdetailspage.html", username = username, editing_user = editing_user)

@app.route("/adminedit_chosenuser", methods = ["POST"])
def adminedit_chosenuser():
    admin_username = request.cookies.get("username")
    
    user_username = request.form["username"]
    user = dynamodb_userdb.getUserFromUsername(user_username)

    # Edit user's email
    old_email = dynamodb_userdb.getEmailFromUsername(user_username)
    new_email = request.form["email"]

    if(old_email != new_email):
        if(dynamodb_userdb.isNewEmailValid(new_email)):
            dynamodb_userdb.updateUserEmail(user_username, new_email)
        else:
            return render_template("adminedituserdetailspage.html", username = admin_username, 
                                    editing_user = user, errorMessage = "Email already exists!")

    # Edit user's image, only if there is an image uploaded
    new_image = request.files["file"]

    # Check if there is a new image
    if new_image.filename != "":
        # Change image_version number
        curr_image_version = dynamodb_userdb.getImageVersionFromUsername(user_username)
        new_image_version = str(int(curr_image_version) + 1)

        # Update S3 image
        s3_userBucket.updateUserImage(user_username, new_image, curr_image_version, new_image_version)

        # Update DynamoDB image_version variable
        dynamodb_userdb.updateUserImageVersion(user_username, new_image_version)

    # Edit user's password, if field is not empty
    new_password = request.form["password"]
    
    # Check if there is a new password
    if(new_password != ""):
        dynamodb_userdb.updateUserPassword(user_username, new_password)
    
    return redirect(url_for("admindisplayusers_page"))

@app.route("/admindelete_chosenuser/<string:user_username>")
def admindelete_chosenuser(user_username):
    # Delete user image in S3
    image_version = dynamodb_userdb.getImageVersionFromUsername(user_username)
    s3_userBucket.deleteUserImageFromS3(user_username, image_version)

    # Delete user details from User DB
    dynamodb_userdb.deleteUserFromUserDB(user_username)

    return redirect(url_for("admindisplayusers_page"))
