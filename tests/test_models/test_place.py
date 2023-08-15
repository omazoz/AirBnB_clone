#!/usr/bin/python3
"""Import Models for test"""
import unittest
from models.place import Place
from datetime import datetime


class PlaceTestCase(unittest.TestCase):
    """ class for Place Test Case """

    def test_place(self):
        """existince"""
        new = Place()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "city_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "description"))
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertTrue(hasattr(new, "latitude"))
        self.assertTrue(hasattr(new, "longitude"))
        self.assertTrue(hasattr(new, "amenity_ids"))

        """ test type"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.city_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.name, str)
        self.assertIsInstance(new.description, str)
        self.assertIsInstance(new.number_rooms, int)
        self.assertIsInstance(new.number_bathrooms, int)
        self.assertIsInstance(new.max_guest, int)
        self.assertIsInstance(new.price_by_night, int)
        self.assertIsInstance(new.latitude, float)
        self.assertIsInstance(new.longitude, float)
        self.assertIsInstance(new.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
