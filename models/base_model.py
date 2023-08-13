#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """Base class that defines common attributes and
    methods for other classes"""

    def __init__(self, *args, **kwargs):
        """*args and **kwargs are Keyword arguments
        used to create the instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.__class__.__name__}
    - ID: {self.id}\nAttributes: {self.__dict__}"

    def save(self):
        """Updating the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the instance attributes to a dictionary representation"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
