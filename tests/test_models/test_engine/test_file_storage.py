#!/usr/bin/python3

import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    This class contains unit tests for the FileStorage class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

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
            self.assertIn("BaseModel." + obj.id, text)

    def test_storage_reload(self):
        obj = BaseModel()

        storage.save()
        storage.objects = {}
        storage.reload()

        self.assertNotEqual(len(storage.objects), 0)
