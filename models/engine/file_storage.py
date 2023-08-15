#!/usr/bin/python3
""" Import models"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class to handle db"""

    __file_path = "db.json"
    __objects = {}

    def all(self):
        """ show all instance"""
        return self.__objects

    def new(self, obj):
        """ new instance """
        id = obj.to_dict()["id"]
        class_Name = obj.to_dict()["__class__"]
        key_Name = class_Name+"."+id
        self.__objects[key_Name] = obj

    def save(self):
        """ Save instance """
        list_data = dict(self.__objects)
        for k, v in list_data.items():
            list_data[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(list_data, f)

    def reload(self):
        """ reload all instances from json file"""
        list_data = self.__objects
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path) as f:
                    for k, v in json.load(f).items():
                        if "BaseModel" in k:
                            list_data[k] = BaseModel(**v)
                        if "User" in k:
                            list_data[k] = User(**v)
                        if "Place" in k:
                            list_data[k] = Place(**v)
                        if "State" in k:
                            list_data[k] = State(**v)
                        if "City" in k:
                            list_data[k] = City(**v)
                        if "Amenity" in k:
                            list_data[k] = Amenity(**v)
                        if "Review" in k:
                            list_data[k] = Review(**v)
            except Exception:
                pass
