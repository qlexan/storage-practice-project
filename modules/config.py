import os
from dotenv import load_dotenv

load_dotenv() 

DB_PATH = os.getenv("DB_PATH", "db.json") 
DEBUG = os.getenv("DEBUG") == "True"