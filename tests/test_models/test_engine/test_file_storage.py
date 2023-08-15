#!/usr/bin/python3
"""Import Models for test"""
import unittest
from models.base_model import BaseModel
import models
import json
import os
from models import storage

class FileStorageTestCase(unittest.TestCase):
    """ test for FileStorageTestCase"""

    def test_FileStorage_init(self):
        """ test1 """
        f_path = storage._FileStorage__file_path
        objs = storage._FileStorage__objects
        """check class attr"""
        self.assertEqual(f_path, "file.json")
        self.assertIsInstance(f_path, str)
        self.assertIsInstance(objs, dict)
        new = BaseModel()
        """ check if it have methods """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """test all"""
        self.assertIsInstance(storage.all(), dict)
        self.assertNotEqual(storage.all(), {})
        """existence id"""
        self.assertTrue(hasattr(new, "id"))
        self.assertIsInstance(new.id, str)

        """new"""
        key_name = "BaseModel."+new.id
        self.assertIsInstance(storage.all()[key_name], BaseModel)
        self.assertEqual(storage.all()[key_name], new)
        """ check if object exist by key_name """
        self.assertIn(key_name, storage.all())
        """ check if the object found in storage with corrrect id"""
        self.assertTrue(storage.all()[key_name] is new)

        """save"""
        storage.save()
        with open(f_path, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by key_name """
        self.assertIn(key_name, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[key_name], new.to_dict())

        """reload"""
        storage.all().clear()
        storage.reload()
        with open(f_path, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data[key_name],
                         storage.all()[key_name].to_dict())

        """file"""
        if os.path.exists(f_path):
            os.remove(f_path)
        self.assertFalse(os.path.exists(f_path))
        storage.reload()


if __name__ == '__main__':
    unittest.main()
