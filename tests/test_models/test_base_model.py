#!/usr/bin/python3
"""Import Models for test"""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys
from unittest.mock import patch
from models import storage
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """ class for BaseModel Test Case """

    def setUp(self):
        """ class for base test """
        with open(storage._FileStorage__file_path, 'w') as file:
            file.truncate(0)
        storage.all().clear()

    def tearDown(self):
        """ class for base test """
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        """ class for base test """
        nouveau = BaseModel()

        """ check if it have methods """
        self.assertTrue(hasattr(nouveau, "__init__"))
        self.assertTrue(hasattr(nouveau, "__str__"))
        self.assertTrue(hasattr(nouveau, "save"))
        self.assertTrue(hasattr(nouveau, "to_dict"))

        """existince"""
        self.assertTrue(hasattr(nouveau, "id"))
        self.assertTrue(hasattr(nouveau, "created_at"))
        self.assertTrue(hasattr(nouveau, "updated_at"))

        """type test"""
        self.assertIsInstance(nouveau.id, str)
        self.assertIsInstance(nouveau.created_at, datetime)
        self.assertIsInstance(nouveau.updated_at, datetime)

        """ check if save in storage """
        key_name = "BaseModel."+nouveau.id
        """ check if object exist by key_name """
        self.assertIn(key_name, storage.all())
        """ check if the object found in storage with corrrect id"""
        self.assertTrue(storage.all()[key_name] is nouveau)

        """ Test update """
        nouveau.name = "My First Model"
        nouveau.my_number = 89
        self.assertTrue(hasattr(nouveau, "name"))
        self.assertTrue(hasattr(nouveau, "my_number"))
        self.assertTrue(hasattr(storage.all()[key_name], "name"))
        self.assertTrue(hasattr(storage.all()[key_name], "my_number"))

        """check if save() update update_at time change"""
        old_time = nouveau.updated_at
        nouveau.save()
        self.assertNotEqual(old_time, nouveau.updated_at)
        self.assertGreater(nouveau.updated_at, old_time)

        """ check if init it call: models.storage.save() """
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        """check if it save in json file"""
        key_name = "BaseModel."+nouveau.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by key_name """
        self.assertIn(key_name, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[key_name], nouveau.to_dict())

    def test_basemodel_init2(self):
        """ class for base test """

        nouveau = BaseModel()
        nouveau.name = "John"
        nouveau.my_number = 89
        new2 = BaseModel(**nouveau.to_dict())
        self.assertEqual(nouveau.id, new2.id)
        self.assertEqual(nouveau.name, "John")
        self.assertEqual(nouveau.my_number, 89)
        self.assertEqual(nouveau.to_dict(), new2.to_dict())

    def test_basemodel_init3(self):
        """ DOC DOC DOC """
        nouveau = BaseModel()
        new2 = BaseModel(nouveau.to_dict())
        self.assertNotEqual(nouveau, new2)
        self.assertNotEqual(nouveau.id, new2.id)
        self.assertTrue(isinstance(new2.created_at, datetime))
        self.assertTrue(isinstance(new2.updated_at, datetime))

        nouveau = BaseModel()

        self.assertEqual(
            str(nouveau),  "[BaseModel] ({}) {}".format(nouveau.id, nouveau.__dict__))

        old_time = nouveau.updated_at
        nouveau.save()
        self.assertGreater(nouveau.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
