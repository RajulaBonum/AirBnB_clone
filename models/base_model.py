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

    def __init__(self):
        """
        initialize id, created_at, updated_at
        """
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
        mydict['__class_'] = self.__class__.__name__
        mydict['create_at'] = self.created_at.isoformat()
        mydict['updated_at'] = self.updated_at.isoformat()
        return mydict
