#!/usr/bin/python3

import os
import unittest

from models import storage
from models.state import State


class TestAmenity(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_name(self):
        state_model = State()
        state_model.name = "Test"
        self.assertEqual(state_model.name, "Test")
