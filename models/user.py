#!/usr/bin/python3
'''Import several library'''
from models.base_model import BaseModel
'''Create the class user'''


class User(BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
