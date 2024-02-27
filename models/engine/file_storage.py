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
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        pass
