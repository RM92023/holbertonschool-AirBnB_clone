#!/usr/bin/python3
'''Import several library'''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
'''Create the class user'''

class User(BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''