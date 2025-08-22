import os
from dotenv import load_dotenv

load_dotenv() 

DB_PATH = os.getenv("DB_PATH", "db.json") 
SHELF_PATH = os.getenv("SHELF_PATH", "shelf.json") 
DEBUG = os.getenv("DEBUG") == "True"