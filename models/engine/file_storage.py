#!/usr/bin/python3

from models.base_model import BaseModel
import json
# This function  serializes instances to a JSON file and deserializes JSON file to instances

class FileStorage:
    __file_path = file.json()
    __objects = {}

def all(self):
    # returns the dictionary
    return self.__objects

def new(self, obj):
   # sets in __objects the obj with key <obj class name>.id
   key = "{}.{}".format(obj.__class__.__name__, obj.id)
   self.__objects[key] = obj 

def save(self):
    # serializes __objects to the JSON file (path: __file_path)
    obj_dict = {key: obj.to_dict() for key, obj in self.__objects.item()}
    with open(self.__file_path, 'w') as file:
        json.dump(obj_dict, file, indent=4)
def reload(self):
    # deserializes the JSON file to __objects
    try:
        with open(self.__file_path, 'r') as file:
            obj_dict = json.load(file)
            for key, obj_dict in self.__objects.item()
            class_name = key.split('.')[0]
            class_ = eval(class_name)
            obj = class(**obj_dict)
            self.__objects[key] = obj
    except FileNotFoundError:
        pass


