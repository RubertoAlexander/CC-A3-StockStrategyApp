import boto3

OUR_ADDRESS = "stansup123@gmail.com"

SUBJECT = "Welcome to STAN!"

BODY = ""

BODYHTML = """<html>
<head></head>
<body>
  <h3>This email is sent with Amazon SES</h3>

  <p>Welcome welcome. Please do not misuse our APIs as it costs money :')</p>
</body>
</html>
"""

CHARSET = "UTF-8"

ses = boto3.client("ses", region_name="us-east-1")

def sendNewUserEmail(user_email):
    ses.send_email(
        Destination = {
            'ToAddresses': [
                user_email,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODYHTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source = OUR_ADDRESS,
    )