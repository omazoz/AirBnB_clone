#!/usr/bin/python3
"""Import Models for test"""
import unittest
from models.review import Review
from datetime import datetime


class ReviewTestCase(unittest.TestCase):
    """ class for Review Test Case"""

    def test_review(self):
        """existince"""
        new = Review()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "place_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "text"))

        """test type """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.place_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.text, str)


if __name__ == '__main__':
    unittest.main()
