#!/usr/bin/python3
"""
'db_storage' Creates a New engine 'DBStorage'
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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

            self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    user, pwd, host, db),
                pool_pre_ping=True)
            session_maker = sessionmaker(bind=self.__engine)
            DBStorage.__session = session_maker()
            if os.getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(bind=self.__engine, checkfirst=True)
        except Exception as err:
            print("Raised an Exception during init:")
            print(err)

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
            session.delete(obj)

    def reload(self):
        """Create all tables in the database and also
        create the current database session using 'sessionmaker'
        and 'scoped_session' to make the Session thread-safe.
        """
        try:
            Base.metadata.create_all(self.__engine)
            session_maker = sessionmaker(self.__engine, expire_on_commit=False)
            session = session_maker()
        except Exception as err:
            print("Exception raised during reload:")
            print(err)
