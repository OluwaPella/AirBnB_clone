#!/usr/bin/python3
"""creates a basemodel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ initiatilizes class basemodel"""

    def __init__(self, *args, **kwargs):
        """ the args in the basemodel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            isoformat = "%Y-%m-%dT%H:%M:%S.%f"

            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(value, isoformat))
                elif key != '__class__':
                    setattr(self, key, value)

        models.storage.new(self)

    def __str__(self):
        """the string representation of the class"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dict representation"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
