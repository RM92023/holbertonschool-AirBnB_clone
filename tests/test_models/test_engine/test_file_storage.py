import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a BaseModel instance for testing.
        """
        self.model = BaseModel()

    def test_save_updates_updated_at(self):
        """
        Test that the save() method updates the updated_at attribute.
        """
        previous_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(previous_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        """
        Test that the to_dict() method returns a dictionary.
        """
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        """
        Test that the to_dict() method returns a dictionary with expected keys.
        """
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        obj_dict = self.model.to_dict()
        for key in expected_keys:
            self.assertIn(key, obj_dict)

    def test_id_is_string(self):
        """
        Test that the id attribute is a string.
        """
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test that the created_at attribute is a datetime object.
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_str_representation(self):
        """
        Test the __str__() method for the BaseModel class.
        """
        expected_string = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_string)


if __name__ == '__main__':
    unittest.main()
