#!/usr/bin/python3
"""Defines the classs review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review."""
    place_id = ""
    user_id = ""
    text = ""
