#!/usr/bin/python3

import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    This class represents a file storage system
    for storing and retrieving objects.
    """

    __file_path = "file.json"
    __objects = {}

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        FileStorage.__objects = value

    def all(self):
        """
        Returns the dictionary of all objects currently stored.
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage system.
        """

        class_name = obj.__class__.__name__
        FileStorage.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """
        Saves the objects in the storage system to a file.
        """

        new_items = {}
        for key, value in FileStorage.__objects.items():
            new_items[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_items, f)

    def reload(self):
        """
        Loads objects from a file into the storage system.
        """

        try:
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)
            for key in objs:
                class_name = key.split(".")[0]
                FileStorage.__objects[key] = eval(f"{class_name}(**objs[key])")
        except Exception:
            pass

# file_storage.py
