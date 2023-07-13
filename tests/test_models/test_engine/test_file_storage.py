import unittest
import json
import os
from datetime import datetime
from time import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.strg = FileStorage()
        self.bmdl = BaseModel()
        self.start = time()

    def tearDown(self):
        self.end = time()

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

    def test_save_method(self):
        Newstorage = FileStorage()
        myModels = BaseModel()
        Newstorage.new(myModels)
        Newstorage.save()
        with open('file.json', 'r') as f:
            json_obj = json.loads(f.read())
        self.assertDictEqual(
            json_obj, {f'BaseModel.{myModels.id}': myModels.to_dict()})
        os.remove('file.json')

    def test_save(self):
        self.strg.new(self.bmdl)
        self.assertEqual(self.strg.save(), None)

    def test_reload(self):
        self.assertEqual(self.strg.reload(), None)
        os.remove('file.json')


if __name__ == '__main__':
    unittest.main()
