#!/usr/bin/python3
'''Import several library'''
import json
import os
from models.base_model import BaseModel
from models.user import User
'''Create to class call Filestorage'''


class FileStorage():
    '''Attributes for tha class'''

    __file_path = 'file.json'
    __objects = {}

    '''Function that return a object'''

    def all(self):
        return self.__objects

    '''sets in __objects the obj with key'''

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    '''Function that serializes __objects to the JSON file '''

    def save(self):
        """"Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, file, indent=4)

    '''deserializes the JSON file to __objects'''

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                loaded = json.load(file)
                for k, v in loaded.items():
                    class_name = v['__class__']
                    obj = eval(class_name)(**v)
                    self.__objects[k] = obj
        else:
            self.__objects = {}
