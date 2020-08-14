# load constants
import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv

dotenv_path = join(abspath(dirname(__file__)), '.env')

load_dotenv(dotenv_path=dotenv_path)

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv('APP_SECRET')
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"

URL_TOKEN="https://www.reddit.com/api/v1/access_token"