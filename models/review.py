#!/usr/bin/python3
"""defines the review attributes"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defines the review attributes"""
    place_id = ""
    user_id = ""
    text = ""
