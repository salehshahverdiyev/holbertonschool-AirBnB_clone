#!/usr/bin/python3

from datetime import datetime
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_setup(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)
    
    def test_created_at(self):
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsInstance(self.base_model.created_at, datetime)
    
    def test_save_method(self):
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
    
    def test_str_method(self):
        expected_string = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_string)
