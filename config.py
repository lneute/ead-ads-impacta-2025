import os
import dotenv
from sqlalchemy.engine import URL

dotenv.load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = URL.create(drivername="postgresql+psycopg2", 
                                  username=os.getenv("SQL_USER"), 
                                  password=os.getenv("SQL_PASSWORD"), 
                                  host=os.getenv("SQL_HOST"), 
                                  port=int(os.getenv("SQL_PORT")), 
                                  database=os.getenv("SQL_DATABASE"))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = "supersegredo"

