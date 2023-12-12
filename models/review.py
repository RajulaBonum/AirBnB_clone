#!/usr/bin/python3
"""class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attribute"""
    place_id = ""
    user_id = ""
    text = ""
