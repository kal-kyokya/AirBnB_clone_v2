#!/usr/bin/python3
from sqlalchemy import create_engine
import os


user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')

engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}")
connection = engine.connect()
print("Connection successful!")
connection.close()
