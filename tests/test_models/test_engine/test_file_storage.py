import unittest
import json
import os
from datetime import datetime
from time import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.start = time()

    def tearDown(self):
        self.end = time()

    def test_file_path(self):
        """
        Test that __file_path attribute is set correctly.
        """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    # def test_objects(self):
    #     """
    #     Test that __objects attribute is an empty dictionary.
    #     """
    #     self.assertEqual(self.storage._FileStorage__objects, {})

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

    # def test_file_storage_methods(self):
    #     """
    #     Testing FileStorage methods
    #     """
    #     storage = FileStorage()
    #     self.assertDictEqual(storage.all(), {})
    #     instanceBM = BaseModel()
    #     self.assertDictEqual(storage.all(),
    #                          {f'BaseModel.{instanceBM.id}': instanceBM})
    #     storage.save()
    #     with open('file.json') as file:
    #         loaded = json.loads(file.read())
    #     self.assertDictEqual(
    #         loaded, {f'BaseModel.{instanceBM.id}': instanceBM.to_dict()})
    #     storage.all().clear()
    #     storage.reload()
    #     self.assertEqual(storage.all().get(
    #         f'BaseModel.{instanceBM.id}').id, instanceBM.id)
    #     storage.all().clear()
    #     os.remove('file.json')

    def test_file_storage_attributes(self):
        """
        Testing FileStorage atributtes
        """
        storage = FileStorage()
        storage.reload()
        storage._FileStorage__objects = {}
        self.assertEqual(storage._FileStorage__file_path, 'file.json')
        self.assertEqual(storage._FileStorage__objects, {})

    def test_save(self):
        self.base_model.updated_at = datetime.utcnow()
        self.storage.new(self.base_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            key = "{}.{}".format(
                type(self.base_model).__name__, self.base_model.id)
            self.assertIn(key, data)
            self.assertEqual(data[key], self.base_model.to_dict())

    def test_reload(self):
        self.assertEqual(self.storage.reload(), None)
        os.remove('file.json')


if __name__ == '__main__':
    unittest.main()
