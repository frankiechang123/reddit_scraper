from constants import *
import requests
import requests.auth


class reddit_spider:

    def __init__(self):
        response = self.getAuth()
        self.token = response["access_token"]
        self.token_type = response["token_type"]

    # get the authentication info
    def getAuth(self):
        client_auth = requests.auth.HTTPBasicAuth(APP_ID, APP_SECRET)
        post_data = {"grant_type": "password",
                     "username": USER_NAME, "password": PASSWORD}
        headers = {"User-Agent": USER_AGENT}

        response = requests.post(URL_TOKEN, data=post_data,
                                 auth=client_auth, headers=headers)
        return response.json()

    # returns a list of IDs of the posts in the subreddit
    # Mode: hot, best, new
    def get_Post_IDs(self, subreddit=None, count=25, mode="hot"):
        if(subreddit):
            sub_url = "r/{subreddit}/"
        else:
            sub_url = ""

        # validate count
        if(count < 0):
            count = 0

        # validate mode
        if(mode == "hot"):
            suffix = "hot.json"
        elif(mode == "new"):
            suffix = "new.json"
        elif(mode == "best"):
            suffix = "best.json"
        else:
            print("invalid mode")
            return None


spider = reddit_spider()
print(spider.token)
print(spider.token_type)
