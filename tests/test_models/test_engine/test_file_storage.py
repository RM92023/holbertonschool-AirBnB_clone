import unittest
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def test_reload(self):
        # Crea un archivo JSON con un objeto guardado
        data = {
            'BaseModel.123456': {
                'id': '123456',
                'name': 'objeto1',
                # ...otros atributos...
            }
        }
        with open(self.file_storage._FileStorage__file_path, 'w') as file:
            json.dump(data, file)

        # Llama al método reload() para cargar los objetos en la instancia de FileStorage
        self.file_storage.reload()
        
        # Comprueba que el objeto se cargó correctamente
        objects = self.file_storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn('BaseModel.123456', objects)
        self.assertEqual(objects['BaseModel.123456'].name, 'objeto1')


if __name__ == '__main__':
    unittest.main()
