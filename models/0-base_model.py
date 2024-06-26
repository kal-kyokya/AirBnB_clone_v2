#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates 'updated_at' with current time when instance is changed"""
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        value = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary.update({'__class__': value})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary


"""
print(f"{type(dict()).__name__}")
print(f"{type(dict())}")
print((str(type(dict()))))
print((str(type(dict())).split('.')[-1]))
foo1 = (str(type(dict())).split('.')[-1]).split('\'')[0]
foo = (str(type(dict())).split('.')[-1]).split('\'')[1]
print(f"Here is {foo1}$")
print(f"Here is {foo}")
"""
