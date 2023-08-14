#!/usr/bin/python3
"""creates a basemodel class"""
import uuid
from datetime import datetime

class BaseModel:
    """
    Base class that defines common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        *args and **kwargs are Keyword arguments used to create the instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        import models
        """
        Updating the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
    def to_dict(self):
        """
        Converts the instance attributes to a dictionary representation
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict                                          
