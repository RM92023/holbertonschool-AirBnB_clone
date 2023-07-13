import datetime
import unittest
import os
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):

        self.file_path = os.path.join(os.getcwd(), "test_file.json")
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_path_default_value(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_file_path(self):
        """
        Test that __file_path attribute is set correctly.
        """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_all_returns_dictionary_of_objects(self):
        self.storage.new(self.base_model)
        objects = self.storage.all()
        self.assertEqual(
            objects, {f"BaseModel.{self.base_model.id}": self.base_model})

    def test_new_adds_object_to_objects_dictionary(self):
        self.storage.new(self.base_model)
        expected_key = f"BaseModel.{self.base_model.id}"
        self.assertIn(expected_key, self.storage._FileStorage__objects)
        self.assertEqual(
            str(self.storage._FileStorage__objects[expected_key]),
            str(self.base_model)
        )

    def test_file_path_none_returns_ok(self):
        storage = FileStorage()
        storage._FileStorage__file_path = None
        result = storage.save()
        self.assertEqual(result, "OK")


if __name__ == '__main__':
    unittest.main()
