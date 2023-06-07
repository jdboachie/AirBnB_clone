#!/usr/bin/python3
"""
Defines a class TestBaseModel.
"""

import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        """Test that a new BaseModel instance is initialized correctly"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.id, str)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsNotNone(base_model.updated_at)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_string_representation(self):
        """Test the string representation of a BaseModel instance"""
        base_model = BaseModel()
        expected_string = "[BaseModel] ({}) {}".format(
            base_model.id,
            base_model.__dict__
        )
        self.assertEqual(str(base_model), expected_string)

    def test_save(self):
        """Test the save method of a BaseModel instance"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        sleep(1)
        base_model.save()
        self.assertNotEqual(base_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of a BaseModel instance"""
        base_model = BaseModel()
        expected_dict = {
            'id': base_model.id,
            'created_at': base_model.created_at.isoformat(),
            'updated_at': base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
