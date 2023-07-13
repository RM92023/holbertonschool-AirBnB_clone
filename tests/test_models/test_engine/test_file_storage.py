import unittest
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def test_file_path(self):
        """
        Test that __file_path attribute is set correctly.
        """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """
        Test that __objects attribute is an empty dictionary.
        """
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all(self):
        """
        Test the all() method returns the __objects dictionary.
        """
        all_objs = self.storage.all()
        self.assertEqual(all_objs, self.storage._FileStorage__objects)

    def test_new(self):
        """
        Test that new() method adds a new object to __objects.
        """
        my_model = BaseModel()
        self.storage.new(my_model)
        key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_file_storage_attributes(self):
        """
        Testing FileStorage atributtes
        """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, 'file.json')

    def test_file_storage_methods(self):
        """
        Testing FileStorage methods
        """
        storage = FileStorage()
        instanceBM = BaseModel()
        storage.save()
        with open('file.json') as file:
            loaded = json.loads(file.read())
        storage.all().clear()
        storage.reload()
        self.assertEqual(storage.all().get(
            f'BaseModel.{instanceBM.id}').id, instanceBM.id)
        storage.all().clear()
        os.remove('file.json')

    def test_save(self):
        """
        Test that save() method updates the updated_at attribute.
        """
        BaseModel = getattr(__import__('models.tmp_base_model'), 'BaseModel')
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        updated_at_after_save = my_model.updated_at
        self.assertNotEqual(initial_updated_at, updated_at_after_save)
        self.assertIsInstance(updated_at_after_save, datetime)
        self.assertEqual(my_model.save(), None)

if __name__ == '__main__':
    unittest.main()
