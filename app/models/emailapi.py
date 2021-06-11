import requests

from app.models import config

def sendEmail(name, email, subject, message):
    url = "https://email-sender1.p.rapidapi.com/"

    querystring = {"txt_msg":message,"to":"stansup123@gmail.com","from":name,"subject":subject}

    headers = {
        'x-rapidapi-key': config.emailAPI_key(),
        'x-rapidapi-host': "email-sender1.p.rapidapi.com"
    }

    requests.request("POST", url, headers = headers, params = querystring)
