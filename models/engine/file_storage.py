#!/usr/bin/python3
'''Import several library'''
import json
import os
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
        """
        This method saves the dictionary of objects to the JSON file.
        """
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as fl:
            json.dump(objects_dict, fl, indent=4)

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
