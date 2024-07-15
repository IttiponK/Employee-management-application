import os 
from dotenv import load_dotenv

load_dotenv('infrastructure/config/.env')

BUCKET_NAME = os.environ['BUCKET_NAME']

BUCKET_URL = os.environ['BUCKET_URL']

TERMINATE_STATUS = 1

APP_SECRET = os.environ['APP_SECRET']