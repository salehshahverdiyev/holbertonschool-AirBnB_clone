#!/usr/bin/python3

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        FileStorage.__objects = {}

    def test_check_type(self):
        self.assertEqual(str, type(FileStorage.__file_path))
        self.assertEqual(dict, type(FileStorage.__objects))

    def test_storage_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)

        all_objects = storage.all()

        self.assertIn(obj1, all_objects.values())
        self.assertIn(obj2, all_objects.values())

    def test_storage_new(self):
        obj = BaseModel()
        storage.new(obj)

        self.assertIn(obj, storage.all().values())

    def test_storage_save(self):
        obj = BaseModel()

        storage.new(obj)
        storage.save()

        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("BaseMode." + obj.id, text)
