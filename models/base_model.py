#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
      """
    Base class that defines common attributes and methods for other classes"""
    def __int__ = (self, *arg, **kwargs):
        """*arg and **kwargs are Keyword arguments used to create the instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
       
       if kwargs:
           for key, value in kwargs.item():
               if key == 'created_at' or 'updated_at':
                   setattr(self, key , datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
               else
               self.id = str(uuid.uuid4())
               self.created_at = self.updated_at = datetime.now()
               def __str__ = (self):
                   """Returns a string representation of the instance"""
                   return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
               def save(self):
                   """updateing the public instance attribute updated_at with the current datetime"""
                   self.updated_at = datetime.now()
                   to_dict(self):
                        """Converts the instance attributes to a dictionary representation"""
                      ob_dict = self.__dict__.copy()
                      ob_dict['__class__'] = self.__class__.__name_
                      ob_dict['created_at'] = self.created_at.isoformat()
                      ob_dict['updated_at'] = seld.updated_at.isoformat()
                      return ob_dict
