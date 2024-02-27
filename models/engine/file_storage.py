#!/usr/bin/python3


import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        class_name = obj.__class__.__name__
        FileStorage.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        new_items = {}
        for key, value in FileStorage.__objects.items():
            new_items[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_items, f)

    def reload(self):
        pass
