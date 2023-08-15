#!/usr/bin/python3
"""Import Models for test"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ class for amenity test """

    def test_amenity(self):
        """existince"""
        nouveau = Amenity()
        self.assertTrue(hasattr(nouveau, "id"))
        self.assertTrue(hasattr(nouveau, "created_at"))
        self.assertTrue(hasattr(nouveau, "updated_at"))
        self.assertTrue(hasattr(nouveau, "name"))

        """type test"""
        self.assertIsInstance(nouveau.id, str)
        self.assertIsInstance(nouveau.created_at, datetime)
        self.assertIsInstance(nouveau.updated_at, datetime)
        self.assertIsInstance(nouveau.name, str)


if __name__ == '__main__':
    unittest.main()
