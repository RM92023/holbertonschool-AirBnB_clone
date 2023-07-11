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
    
    def test_id(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)


if __name__ == "__main__":
    unittest.main()
