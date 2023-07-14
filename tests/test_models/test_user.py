#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Testing User functionality """

    def setUp(self):
        """ Setup """
        self.user1 = User()
        self.user2 = User()
        self.user2.email = "user@example.com"
        self.user2.password = "password"
        self.user2.first_name = "Betty"
        self.user2.last_name = "Holberton"
        self.user2.save()

    def test_attributes(self):
        """ Test attributes """
        self.assertTrue(hasattr(self.user1, "email"))
        self.assertTrue(hasattr(self.user1, "password"))
        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertTrue(hasattr(self.user1, "last_name"))

    def test_id(self):
        """ Test id """
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_attributes_default(self):
        """ Test attributes default """
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")

    def test_created_at(self):
        """ Test created_at """
        self.assertNotEqual(self.user1.created_at, self.user2.created_at)

    def test_str(self):
        """ Test str """
        expected = f"[{type(self.user2).__name__}] ({self.user2.id}) {self.user2.__dict__}"
        self.assertEqual(str(self.user2), expected)

    def test_save(self):
        """ Test save """
        created_at = self.user1.created_at
        updated_at = self.user1.updated_at
        self.user1.save()
        self.assertEqual(created_at, self.user1.created_at)
        self.assertNotEqual(updated_at, self.user1.updated_at)

    def to_dict(self):
        """ Returns the dictionary representation of the model """
        dict_ = {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        dict_["__class__"] = type(self).__name__
        return dict_


if __name__ == '__main__':
    unittest.main()
