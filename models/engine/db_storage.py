#!/usr/bin/python3
"""
'db_storage' Creates a New engine 'DBStorage'
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class DBStorage():
    """Database Engine used to stored ORM results."""

    __engine = None
    __session = None

    __classes = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        """Initializes class instances' public attributes."""
        try:
            user = os.getenv('HBNB_MYSQL_USER')
            pwd = os.getenv('HBNB_MYSQL_PWD')
            host = os.getenv('HBNB_MYSQL_HOST')
            db = os.getenv('HBNB_MYSQL_DB')

            mandatory = [user, pwd, host, db]
            if not all(mandatory):
                print("Ensure proper setting of environment variables.")
                return

            self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                          format(user, pwd, host, db),
                                          pool_pre_ping=True)

            if os.getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(bind=self.__engine, checkfirst=True)
        except Exception as err:
            print("Raised an Exception during init:")
            print(type(err))
            print(err)

    def all(self, cls=None):
        """Retrieves objects from the database storage.

        Arg:
            cls: Class name for all object to be retrieve.
        """
        new_dict = {}
        for class_value in self.__classes:
            if cls is None or cls is class_value:
                objs = self.__session.query(class_value).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """Adds an object to the current Database session.

        Arg:
            obj: Name of the object to be added to the Database.
        """
        if obj and self.__session:
            self.__session.add(obj)

    def save(self):
        """Commits all changes to the current Database session."""
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current Database session.

        Arg:
            obj: Name of the object to be deleted.
        """
        if obj and self.__session:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        try:
            Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session
        except Exception as err:
            print("Exception raised during reload:")
            print(err)

    def close(self):
        """Call remove() method on the class attribute 'session'."""
        self.__session.remove()
