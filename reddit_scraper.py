from constants import *
import requests
import requests.auth

#return the authentication info
def getAuth():
    client_auth = requests.auth.HTTPBasicAuth(APP_ID, APP_SECRET)
    post_data = {"grant_type": "password",
             "username": USER_NAME, "password": PASSWORD}
    headers = {"User-Agent": USER_AGENT}

    response=requests.post(URL_TOKEN,data=post_data,auth=client_auth,headers=headers)
    return response.json()

print(getAuth())