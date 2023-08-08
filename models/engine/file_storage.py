#!/usr/bin/python3
"""Import lib for FileStorage Class"""
import json
from models.base_model import BaseModel
import os.path


class FileStorage:
    """Class FileStorage"""

    __file_path = "db.json"
    __objects = {}

    def all(self):
        """Return __objects"""
        return self.__objects
    
    def new(self,obj):
        """sets in __objects the obj with key <obj class name>.id"""
        for o in obj.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.__objects["{}.{}".format(class_name, o.id)] = o        

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        d = self.__objects
        object_dict = {obj: d[obj].to_dict() for obj in d.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(object_dict, f)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                object_dict = json.load(f)
                self.new(object_dict)
        else:
             print("File Not exist")
