#!/usr/bin/python3
"""Module for class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """ class BaseModel that defines all common 
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at"  or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value


    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at 
        with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values 
        of __dict__ of the instance"""
        copy_dict = self.__dict__.copy()
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        copy_dict["__class__"] = self.__class__.__name__
        return copy_dict
