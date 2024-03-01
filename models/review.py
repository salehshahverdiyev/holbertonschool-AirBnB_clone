#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class represents a review for a place in the AirBnB clone project.
    """

    place_id = ""
    user_id = ""
    text = ""
