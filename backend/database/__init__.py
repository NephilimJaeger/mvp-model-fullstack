from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from .db_models import Base


DB_PATH = "./backend/database"
DB_URL = f"sqlite:///{DB_PATH}/neo.db"

engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

if not database_exists(engine.url):
    create_database(engine.url)
    print(f"Database created at {DB_URL}")

Base.metadata.create_all(engine)
