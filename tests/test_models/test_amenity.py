#!/usr/bin/python3

import os
import unittest

from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(Amenity.name, str)

    def test_name(self):
        amenity_model = Amenity()
        amenity_model.name = "Test"
        self.assertEqual(amenity_model.name, "Test")
