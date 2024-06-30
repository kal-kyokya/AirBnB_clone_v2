#!/usr/bin/python3
"""
'db_storage' Creates a New engine 'DBStorage'
"""
from sqlalchemy import create_engine


class DBStorage():
    """Database Engine used to stored ORM results."""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes class instances' public attributes."""
        DBStorage.__engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
            ),
            pool_pre_ping=True)

    def all(self, cls=None):
        """Retrieves objects from the database storage.

        Arg:
            cls: Class name for all object to be retrieve.
        """
        pass
