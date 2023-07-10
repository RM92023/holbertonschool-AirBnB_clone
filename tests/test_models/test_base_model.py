import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def TestSave(self):
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)
