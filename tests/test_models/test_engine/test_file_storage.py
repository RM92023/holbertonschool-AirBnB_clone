import unittest
import json
import os
from datetime import datetime
from time import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


import models
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


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

    # def test_file_storage_attributes(self):
    #     """
    #     Testing FileStorage atributtes
    #     """
    #     storage = FileStorage()
    #     self.assertEqual(storage._FileStorage__file_path, 'file.json')
    #     self.assertDictEqual(storage._FileStorage__objects, {})

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

    def test_save(self):
        self.base_model.updated_at = datetime.utcnow()
        self.storage.new(self.base_model)
        self.assertEqual(self.storage.save(), None)
    
    def test_save_method(self):
        """Time to deal with reload() method in FileStorage class"""
        character_bm = BaseModel()
        character_user = User()
        character_state = State()
        character_city = City()
        character_place = Place()
        character_review = Review()
        character_amenity = Amenity()

        models.storage.save()

        # Checks that the objects created above are stored already
        self.assertIn("BaseModel." + character_bm.id,
                      models.storage.all().keys())
        self.assertIn(character_bm, models.storage.all().values())
        self.assertIn("User." + character_user.id, models.storage.all().keys())
        self.assertIn(character_user, models.storage.all().values())
        self.assertIn("State." + character_state.id, models.storage.all().keys())
        self.assertIn(character_state, models.storage.all().values())
        self.assertIn("Place." + character_place.id, models.storage.all().keys())
        self.assertIn(character_place, models.storage.all().values())
        self.assertIn("City." + character_city.id, models.storage.all().keys())
        self.assertIn(character_city, models.storage.all().values())
        self.assertIn("Amenity." + character_amenity.id,
                      models.storage.all().keys())
        self.assertIn(character_amenity, models.storage.all().values())
        self.assertIn("Review." + character_review.id,
                      models.storage.all().keys())
        self.assertIn(character_review, models.storage.all().values())

        # What if more than one arg were passed to this guy?
        # TypeError, we need you here!
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

        # What if None was passed? That guy needs learn a lesson...
        # AttributeError, will you join us?
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_reload(self):
        self.assertEqual(self.storage.reload(), None)
        os.remove('file.json')


if __name__ == '__main__':
    unittest.main()
