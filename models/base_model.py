#!/usr/bin/python3
"""
Class BaseModel that defines common attributes/methods for other classes
Defines Public instances and methods
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Public instance attributes
    """

    def __init__(self, *args, **kwargs):
        """
        initialize id, created_at, updated_at
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """prints class name, self.id and dictionarry representation"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    """
    Public instance methods
    """

    def save(self):
        """Updates (update_at) with current time"""
        self.update_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of instance
        """
        mydict = self.__dict__.copy()
        mydict["__class__"] = type(self).__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
