#!/usr/bin/python3
"""
defines the filestogare class
"""
import json
from os import path
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Returns a FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {key: val.to_dict() for key, val in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __object"""
        if path.exists(self.__file_path) is True:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_d = json.load(f)
                for obj in obj_d.values():
                    cls = obj["__class__"]
                    self.new(eval(cls)(**obj))
