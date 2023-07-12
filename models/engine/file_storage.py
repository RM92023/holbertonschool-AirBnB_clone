#!/usr/bin/python3
'''Import several library'''
import json
from models.base_model import BaseModel
'''Create to class call Filestorage'''


class FileStorage:
    '''Attributes for tha class'''
    classes = {
    'BaseModel': BaseModel,
    }
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
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()

    

    '''deserializes the JSON file to __objects'''
    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals().get(class_name)
                    if class_obj:
                        instance = class_obj(**value)
                        self.new(instance)
        except FileNotFoundError:
            pass
