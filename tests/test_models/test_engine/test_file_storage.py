import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

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

    def test_save(self):
        """
        Test that save() method saves the objects to the file.
        """
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = file.read()
        self.assertNotEqual(data, "")

    def test_reload(self):
        """
        Test that reload() method reloads the objects from the file.
        """
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertIn(key, all_objs)


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        Test that __init__() initializes the instance correctly.
        """
        my_model = BaseModel(name="Test", value=10)
        self.assertEqual(my_model.name, "Test")
        self.assertEqual(my_model.value, 10)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_save(self):
        """
        Test that save() method updates the updated_at attribute.
        """
        my_model = BaseModel()
        previous_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(previous_updated_at, my_model.updated_at)


if __name__ == '__main__':
    unittest.main()