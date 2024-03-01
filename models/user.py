#!/usr/bin/python3


from models.base_model import BaseModel


class User(BaseModel):
    """
    This class represents a user in the AirBnB clone application.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

# user.py
