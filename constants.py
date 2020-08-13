# load constants
import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv

dotenv_path = join(abspath(dirname(__file__)), '.env')

load_dotenv(dotenv_path=dotenv_path)

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv('APP_SECRET')
USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
