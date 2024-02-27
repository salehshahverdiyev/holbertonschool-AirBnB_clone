#!/usr/bin/python3

import os
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        FileStorage.__objects = {}

    def test_id_generation(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.id, str)
    
    def test_created_at(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.created_at)
        self.assertIsInstance(base_model.created_at, datetime)

    def test_save_method(self):
        base_model = BaseModel()
        previous_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(previous_updated_at, base_model.updated_at)

    def test_save_method_with_storage(self):
        base_model = BaseModel()
        base_model.name = "My_First_Model"
        base_model.my_number = 89
        base_model.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIn("BaseModel." + base_model.id, storage.all())

    def test_to_dict_method(self):
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_str_method(self):
        base_model = BaseModel()
        expected_string = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_string)
