#!/usr/bin/python3

import os
import unittest

from models import storage
from models.state import State


class TestAmenity(unittest.TestCase):
    """
    This class contains unit tests for the State class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(State.name, str)

    def test_name(self):
        state_model = State()
        state_model.name = "Test"
        self.assertEqual(state_model.name, "Test")

# test_state.py
