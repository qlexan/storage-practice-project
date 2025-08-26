import os
from dotenv import load_dotenv

load_dotenv() 

DB_PATH = os.getenv("DB_PATH") 
SHELF_PATH = os.getenv("SHELF_PATH") 
DEBUG = os.getenv("DEBUG") == "True"