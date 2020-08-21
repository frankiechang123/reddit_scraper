import matplotlib.pyplot as plt
import wordcloud
from constants import *
import requests
import requests.auth
import html
import csv
import os
import re


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
            sub_url = "r/{0}/".format(subreddit)
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

        url = REDDIT_URL+sub_url+suffix
        headers = {
            "Authorization": "{0}{1}".format(self.token_type, self.token),
            "User-Agent": USER_AGENT
        }
        IDs = []
        if(count <= 100):
            params = {
                "limit": count
            }
            response = requests.request(
                "GET", url, headers=headers, params=params)

            response = response.json()
            if(response.get("error")):
                print(response["message"])
                exit()

            for post in response["data"]["children"]:
                IDs.append(post["data"]["id"])
        else:  # count>100
            _next = None
            while(count > 0):
                if(count >= 100):
                    limit = 100
                else:
                    limit = count
                params = {
                    "limit": limit,
                    "after": _next
                }
                response = requests.request(
                    "GET", url, headers=headers, params=params)

                response = response.json()
                if(response.get("error")):
                    print(response["message"])
                    exit()
                for post in response["data"]["children"]:
                    IDs.append(post["data"]["id"])
                _next = response["data"]["after"]
                count -= limit

        return IDs

    # input: post_id, name of subreddit
    # return a list of comments

    def getComments(self, post_id, subreddit=None):
        if(subreddit):
            url = REDDIT_URL + \
                "r/{0}/comments/{1}.json".format(subreddit, post_id)
        else:  # TODO
            url = REDDIT_URL+"comments/{0}.json".format(post_id)

        headers = {
            "Authorization": "{0}{1}".format(self.token_type, self.token),
            "User-Agent": USER_AGENT
        }
        params = {
            "threaded": False
        }

        response = requests.request("GET", url, headers=headers, params=params)
        response = response.json()

        commentList = []
        PostText = response[0]["data"]["children"][0]["data"]["selftext"]

        commentList.append(toPlainText(PostText))

        commentsJsonList = response[1]["data"]["children"]

        for item in commentsJsonList:
            self.parseComment(commentList, item)

        return commentList

    # input: commentList: list of fetched comments | commentDict: a comment dict
    # commentList gets modified in-place

    def parseComment(self, commentList, commentDict):
        kind = commentDict["kind"]
        if(kind == 'more'):  # TODO: process "more"
            return
        # if(kind=='t1'):
        body = commentDict["data"]["body"]
        text = toPlainText(body)
        commentList.append(text)

    # input:  list of post_IDs, name of subreddit
    # write everything to a csv file
    # output: number of text processed
    def getComments_with_postIDs(self, Post_IDs, subreddit=None):
        count = 0
        for ID in Post_IDs:
            comments = self.getComments(ID, subreddit=subreddit)
            writeToCSV(comments)
            count += len(comments)
        return count

# TODO


def toPlainText(s):
    s = html.unescape(s.replace('\n', ' '))
    s = re.sub(r"&#x200B;", ' ', s)
    s = re.sub(r'https?\S+', "", s)
    return s

# input:  List of text
# write text to text.csv


def writeToCSV(textList):
    with open('text.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(textList)

# delete the file if the csv file exists


def initCsv():
    if(os.path.exists('text.csv')):
        os.remove('text.csv')


initCsv()
spider = reddit_spider()
print(spider.token)
print(spider.token_type)
ids = spider.get_Post_IDs(subreddit="Python", count=150)

print(spider.getComments_with_postIDs(ids))


text = ''
with open('text.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        text += ' '.join(row)

cloud = wordcloud.WordCloud(width=1200, height=600,
                            max_words=100, background_color="white", include_numbers=False, min_word_length=3).generate(text)

plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')


plt.show()


# print(spider.getComments_with_postIDs(ids))
