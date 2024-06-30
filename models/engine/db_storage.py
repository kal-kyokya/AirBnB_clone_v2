#!/usr/bin/python3
"""
'db_storage' Creates a New engine 'DBStorage'
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import BaseModel, Base


class DBStorage():
    """Database Engine used to stored ORM results."""

    __engine = None
    __session = None

    __classes = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        """Initializes class instances' public attributes."""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        mandatory = [user, pwd, host, db]
        if not all(mandatory):
            print("Ensure proper setting of environment variables.")
            return

        with DBStorage.__engine as eng:
            eng = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    user, pwd, host, db),
                pool_pre_ping=True)
            session_maker = sessionmaker(bind=eng)
            DBStorage.__session = session_maker()
            if os.getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(bind=eng, checkfirst=True)

    def all(self, cls=None):
        """Retrieves objects from the database storage.

        Arg:
            cls: Class name for all object to be retrieve.
        """
        with DBStorage.__session as sess:
            results = []
            if cls:
                results = sess.query(cls).all()
            else:
                for value in self.__classes:
                    for obj in sess.query(value):
                        results.append(obj)

            return {"{}.{}".format(
                obj.__class__.__name__, obj.id): obj for obj in results}
