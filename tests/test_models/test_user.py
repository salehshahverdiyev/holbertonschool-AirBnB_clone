#!/usr/bin/python3

import os
import unittest

from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """
    This class contains unit tests for the User class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_email(self):
        user_model = User()
        user_model.email = "test@gmail.com"
        self.assertEqual(user_model.email, "test@gmail.com")

    def test_password(self):
        user_model = User()
        user_model.password = "test"
        self.assertEqual(user_model.password, "test")

    def test_first_name(self):
        user_model = User()
        user_model.first_name = "Test"
        self.assertEqual(user_model.first_name, "Test")

    def test_last_name(self):
        user_model = User()
        user_model.last_name = "Test"
        self.assertEqual(user_model.last_name, "Test")
