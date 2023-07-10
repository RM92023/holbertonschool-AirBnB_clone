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

    def test_to_dict(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        obj = self.base_model.to_dict()
        self.assertEqual(sorted(obj.keys()), sorted(expected_keys))
        self.assertEqual(obj['__class__'], 'BaseModel')
        self.assertIsInstance(obj['created_at'], str)
        self.assertIsInstance(obj['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
