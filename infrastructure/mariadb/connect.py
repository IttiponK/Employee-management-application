from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 

from dotenv import load_dotenv
    
load_dotenv('infrastructure/config/.env')

USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://test:test@localhost:3306/test"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://ittimoo:ittimoo@localhost:3306/vehicleservice"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db_sess():
    db = SessionLocal()
    return db 
        
if __name__ == '__main__':
    
    # print(os.environ['DB_HOST'])
    Base.metadata.create_all(engine)
        
  
  
        