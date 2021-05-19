# from . import s3

import boto3
import os
from werkzeug.utils import secure_filename

s3 = boto3.resource("s3", region_name="us-east-1")

userimage_bucket = "a3-userimage"
imagefile_directory = "tmp/images"

import os.path

def addUserImage(username, imagefile):                                            
    imagefile_name = secure_filename(imagefile.filename)

    current_directory = os.getcwd()

    file_directory = os.path.join(current_directory, imagefile_name)

    imagefile.save(file_directory)

    # Upload to s3
    s3filename = username + "_image.jpg"

    s3.Bucket(userimage_bucket).upload_file(file_directory, s3filename, 
                                            ExtraArgs = {'ACL': 'public-read', 'ContentType': 'image/jpg'})