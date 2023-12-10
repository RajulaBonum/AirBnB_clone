#!/usr/bin/python3
"""
class FileStorage
The class will serialize instances to JSON
The class will also deserialze JSON to instances
"""
import json


class FileStorage:
    """
    Private class attributes
    """
    __file_path = "file.json"
    ___objects = {}

    """
    Public instance methods
    """
    def all(self):
        """returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in (__objects) obj with key (<obj class nem>.id)"""
        key = "{}.{}".format(self.__class__.__name__, self.id)
        self.__objects[key] = obj

    def save(self):
        """serializes objects to JSON FILE(__file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            loaded = {k: v.to_dict() for k, in self.__objects.items()}
            json.dump(loaded, f)

    def reload(self):
        """deserializes te JSON file to __objects"""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            unloaded = json.load(f)
            unloaded = {k: self.classes()[v["__class__"]](**v)
                        for key, value in unloaded.items()}
            """Can or should this overwrite or insert?"""
            self.__objects = unloaded
