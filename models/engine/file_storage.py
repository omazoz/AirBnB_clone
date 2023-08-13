#!/usr/bin/python3
"""Import lib for FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
import os.path


class FileStorage:
    """Class FileStorage"""

    __file_path = "db.json"
    __objects = {}

    def all(self):
        """Return __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def newreload(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        for o in obj.values():
            class_name = o["__class__"]
            del o["__class__"]
            self.__objects["{}.{}".format(class_name, o["id"])] = o
        # print(self.__objects)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        d = {}
        for k, v in self.__objects.items():
            d[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                object_dict = json.load(f)
                self.newreload(object_dict)
        else:
            print("File Not exist")
