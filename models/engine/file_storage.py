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
        """
        Save the objects to the file.
        """
        with open(self._FileStorage__file_path, "w") as file:
            file.write(json.dumps(self._FileStorage__objects))
        return None

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
