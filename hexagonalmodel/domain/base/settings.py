import os 
from dotenv import load_dotenv

load_dotenv('infrastructure/config/.env')

BUCKET_NAME = os.environ['BUCKET_NAME']

BUCKET_URL = os.environ['BUCKET_URL']

TERMINATE_STATUS = 1

APP_SECRET = os.environ['APP_SECRET']

DB_USER = os.environ['DB_USER']

DB_PASSWORD = os.environ['DB_PASSWORD']

DB_NAME = os.environ['DB_NAME']

DB_HOST = os.environ['DB_HOST']