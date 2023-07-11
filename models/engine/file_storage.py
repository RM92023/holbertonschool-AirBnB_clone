#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    def __init__(self):
        self._file_path = 'file.json'
        self.__objects = {}
        BaseModel(id)
        super(FileStorage, self).__init__