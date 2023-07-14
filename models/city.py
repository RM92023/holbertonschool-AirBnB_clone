#!/usr/bin/python3
'''Import several library'''
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    '''create lets in class'''
    state_id = ''
    name = ''
