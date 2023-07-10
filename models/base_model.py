#!/usr/bin/python3
'''Important several modules'''
import uuid
from datetime import *


'''Create the class call BaseModel'''


class BaseModel:

    '''Initializate the function init'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    '''Defining the function str'''
    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    '''updates the public instance attribute
    updated_at with the current datetime'''
    def save(self):
        self.updated_at = datetime.now()

    '''returns a dictionary containing all keys/values
    of __dict__ of the instance'''
    def to_dict(self):
        obj = self.__dict__.copy()
        obj['__class__'] = __class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
