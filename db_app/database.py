from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# postgresql part
#from os import environ

#DB_USER = environ.get("DB_USER", "user")
#DB_PASSWORD = environ.get("DB_PASSWORD", "password")
#DB_HOST = environ.get("DB_HOST", "localhost")
#DB_NAME = "task"
###SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
##SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://user:password@localhost/task_db"
#SQLALCHEMY_DATABASE_URL = (
#    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
#)

#engine = create_engine(SQLALCHEMY_DATABASE_URL)


# sqlite part
SQLALCHEMY_DATABASE_URL = 'sqlite:///./task.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# common part
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
