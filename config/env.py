import os
from dotenv import load_dotenv

load_dotenv() 

DB_URL = os.getenv("DB_URL", "db.sqlite") 
if DB_URL is None:
    raise ValueError("DB_URL env variable is not set")

SHELF_PATH = os.getenv("SHELF_PATH") 
DEBUG = os.getenv("DEBUG") == "True"