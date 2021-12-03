from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import time

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# # import psycopg2
# from psycopg2.extras import RealDictCursor
#
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', port=5433, database='fastapi',
#                                 user='postgres', password='kathmandu', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection successful!")
#         break
#     except Exception as error:
#         print("Database connection failed")
#         print("Error:", error)
#         time.sleep(2)

# my_posts = [{'title': 'my first post', 'content': 'there is something', "id": 1}, {
#     'title': 'my second post', 'content': 'something special', "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
