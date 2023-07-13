#!/usr/bin/python3
"""Create class file storage"""

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class that manages the storage
    and retrieval of objects in a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        newObjName = obj.__class__.__name__
        self.__objects["{}.{}".format(newObjName, obj.id)] = obj

    def save(self):

        """Serialize __objects to the JSON file __file_path."""
        if self.__file_path is None:

            return "OK"
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)
            return "OK"

    def load(self):
        """
        Loads the content of the JSON file into the dictionary of objects.
        If the file doesn't exist, no exception is raised.
        """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                self.__objects = {key: self.__create_instance(
                    key, value) for key, value in data.items()}
        except FileNotFoundError:
            pass

    def reload(self):
        """
        Reloads the content of the JSON file into the dictionary of objects.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                try:
                    data = json.load(file)
                    self.__objects = {key: self.__create_instance(
                        key, value) for key, value in data.items()}
                except json.JSONDecodeError:
                    pass
