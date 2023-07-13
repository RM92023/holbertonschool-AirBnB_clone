#!/usr/bin/python3
'''Import several library'''
import json
import os
import importlib
from models.base_model import BaseModel
'''Create to class call Filestorage'''


class FileStorage:
    '''Attributes for tha class'''

    __file_path = 'file.json'
    __objects = {}

    '''Function that return a object'''

    def all(self):
        return self.__objects

    '''sets in __objects the obj with key'''

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    '''Function that serializes __objects to the JSON file '''

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    '''deserializes the JSON file to __objects'''
    def reload(self):
        class_mapping = {
    'BaseModel': BaseModel,
    }
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name = value['__class__']
                        if class_name in class_mapping:
                            class_ = class_mapping[class_name]
                            obj = class_(**value)
                            self.__objects[key] = obj
            except FileNotFoundError:
                return
