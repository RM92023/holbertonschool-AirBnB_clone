#!/usr/bin/python3
'''Import several library'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''create lets in class'''
    place_id = ''
    user_id = ''
    text = ''
