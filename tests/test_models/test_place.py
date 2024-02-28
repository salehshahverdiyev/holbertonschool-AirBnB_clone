#!/usr/bin/python3

import os
import unittest

from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, float)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

    def test_city_id(self):
        place_model = Place()
        place_model.city_id = "123"
        self.assertEqual(place_model.city_id, "123")

    def test_user_id(self):
        place_model = Place()
        place_model.user_id = "123"
        self.assertEqual(place_model.user_id, "123")

    def test_name(self):
        place_model = Place()
        place_model.name = "Test"
        self.assertEqual(place_model.name, "Test")

    def test_description(self):
        place_model = Place()
        place_model.description = "Test"
        self.assertEqual(place_model.description, "Test")

    def test_number_rooms(self):
        place_model = Place()
        place_model.number_rooms = 2
        self.assertEqual(place_model.number_rooms, 2)

    def test_number_bathrooms(self):
        place_model = Place()
        place_model.number_bathrooms = 2
        self.assertEqual(place_model.number_bathrooms, 2)

    def test_max_guest(self):
        place_model = Place()
        place_model.max_guest = 2
        self.assertEqual(place_model.max_guest, 2)

    def test_price_by_night(self):
        place_model = Place()
        place_model.price_by_night = 2
        self.assertEqual(place_model.price_by_night, 2)

    def test_latitude(self):
        place_model = Place()
        place_model.latitude = 2.2
        self.assertEqual(place_model.latitude, 2.2)

    def test_longitude(self):
        place_model = Place()
        place_model.longitude = 2.2
        self.assertEqual(place_model.longitude, 2.2)

    def test_amenity_ids(self):
        place_model = Place()
        place_model.amenity_ids = [1, 2]
        self.assertEqual(place_model.amenity_ids, [1, 2])
