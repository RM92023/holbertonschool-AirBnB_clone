import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def test_init(self):
        self.base_model.save()
        key = "{}.{}".format(
            self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(
            self.storage._FileStorage__objects[key], self.base_model)

    def TestSave(self):
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_id(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_save_updates_updated_at(self):
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

    def test_str(self):
        class_name = self.base_model.__class__.__name__
        expected_output = "[{}] ({}) {}".format(
            class_name, self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_output)

    def test_base_model_save(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        updated_at_after_save = self.base_model.updated_at
        self.assertGreater(updated_at_after_save, initial_updated_at)

    def tearDown(self):
        self.base_model = None


if __name__ == "__main__":
    unittest.main()
