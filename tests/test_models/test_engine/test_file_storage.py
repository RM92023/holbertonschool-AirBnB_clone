import unittest
import json
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        objects = self.storage.all()
        self.assertEqual(objects, self.storage._FileStorage__objects)

    def test_new(self):
        key = "{}.{}".format(
            self.base_model.__class__.__name__, self.base_model.id)
        self.storage.new(self.base_model)
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(
            self.storage._FileStorage__objects[key], self.base_model)

    def test_save(self):
        key = "{}.{}".format(
            self.base_model.__class__.__name__, self.base_model.id)
        self.storage.new(self.base_model)
        self.storage.save()
        with open("file.json", 'r') as file:
            data = file.read()
            self.assertIn(key, data)

    def test_reload(self):
        key = "{}.{}".format(
            self.base_model.__class__.__name__, self.base_model.id)
        obj_dict = {key: self.base_model.to_dict()}
        with open("file.json", 'w') as file:
            file.write(json.dumps(obj_dict))

        # Limpia el diccionario __objects antes de llamar a reload
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(
            self.storage._FileStorage__objects[key].id, self.base_model.id)

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        storage = FileStorage()
        self.base_model.save()
        key = "{}.{}".format(
            self.base_model.__class__.__name__, self.base_model.id)
        storage.reload()
        self.assertIn(key, storage._FileStorage__objects)
        self.assertEqual(
            storage._FileStorage__objects[key].id, self.base_model.id)
        self.assertEqual(
            storage._FileStorage__objects[key].created_at, self.base_model.created_at)
        self.assertEqual(
            storage._FileStorage__objects[key].updated_at, self.base_model.updated_at)

    def test_save(self):
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
