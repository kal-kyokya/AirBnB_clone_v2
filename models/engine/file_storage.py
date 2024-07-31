#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage

        Args:
            cls: Name of the class to matched.
        """
        if cls:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                cls_name = str(cls).split('\'')[1].split('.')[-1]
                cls_in_dict = str(key).split('.')[0]
                if cls_name == cls_in_dict:
                    obj_dict.update({key: value})
            return obj_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Removes an element from out object dictionary.

        Args:
            obj: Name of the object to be removed.
        """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            del FileStorage.__objects[key]

    def close(self):
        """Call reload() for deserializing the JSON file to objects."""
        self.reload()
