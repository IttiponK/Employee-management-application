import os 
from dotenv import load_dotenv

load_dotenv('infrastructure/config/.env')


AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]