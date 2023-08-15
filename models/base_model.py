#!/usr/bin/python3
""" Import Models
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs) -> None:
        """Initialization of BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    self.__dict__[k] = datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k != "__class__":
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Returns the string representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """update the public instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """returns the dict representation of the instance"""
        d = dict(self.__dict__)
        d["__class__"] = self.__class__.__name__
        if not isinstance(d["created_at"], str):
            d["created_at"] = d["created_at"].isoformat()
        if not isinstance(d["updated_at"], str):
            d["updated_at"] = d["updated_at"].isoformat()
        return d
