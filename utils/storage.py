from sqlmodel import create_engine, Session
from config.env import DB_URL, SHELF_PATH



engine = create_engine(DB_URL)

def new_session() -> Session:
    return Session(engine)
    

