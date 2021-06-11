from flask import render_template, request

from app import app

from app.models import dynamodb_userdb, s3_userBucket


@app.route("/updateuserdetail_page")
def updateuserdetail_page():
    username = request.cookies.get("username")
    user = dynamodb_userdb.getUserFromUsername(username)
    
    return render_template("updateuserdetailpage.html", username = username, user = user)

@app.route("/updatedetails", methods = ["POST"])
def updatedetails():
    username = request.cookies.get("username")
    user = dynamodb_userdb.getUserFromUsername(username)

    # Updating email
    email = dynamodb_userdb.getEmailFromUsername(username)
    new_email = request.form["email"]

    if(email != new_email):
        if(dynamodb_userdb.isNewEmailValid(new_email)):
            dynamodb_userdb.updateUserEmail(username, new_email)
        else:
            return render_template("updateuserdetailpage.html", username = username, 
                            user = user, updateMessage = "Email already exists!")

    # Updating image, only if there is an image uploaded
    new_image = request.files["file"]

    # Check if user uploaded image
    if new_image.filename != "":
        # Change image_version number
        curr_image_version = dynamodb_userdb.getImageVersionFromUsername(username)
        new_image_version = str(int(curr_image_version) + 1)

        # Update S3 image
        s3_userBucket.updateUserImage(username, new_image, curr_image_version, new_image_version)

        # Update DynamoDB image_version variable
        dynamodb_userdb.updateUserImageVersion(username, new_image_version)
    
    return render_template("itisupdated_userdetailpage.html", username = username)