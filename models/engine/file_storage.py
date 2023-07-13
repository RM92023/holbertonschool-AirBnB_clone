#!/usr/bin/python3
'''Import several library'''
import json
import os
from models.base_model import BaseModel
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
        """
        This method loads the dictionary of objects from the JSON file.
        """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as fl:
                json_data = json.load(fl)
                for i in json_data.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            return
