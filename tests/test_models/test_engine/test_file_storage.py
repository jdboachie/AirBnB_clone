#!/usr/bin/python3
"""
Defines a class TestFileStorage.
"""

import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the FileStorage class.
    """

    def setUp(self):
        """
        Create a FileStorage instance and a BaseModel instance.
        """
        self.file_storage = FileStorage()
        self.base_model = BaseModel()

    def test_all(self):
        """
        Test the all method of FileStorage.
        """
        all_objs = self.file_storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """
        Test the new method of FileStorage.
        """
        self.assertEqual(len(self.file_storage.all()), 0)
        self.file_storage.new(BaseModel())
        self.assertEqual(len(self.file_storage.all()), 1)

    def test_save(self):
        """
        Test the save method of FileStorage.
        """
        with open(self.file_storage._FileStorage__file_path, "r") as f:
            data = json.load(f)
        self.assertNotIn("BaseModel." + self.base_model.id, data)
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        with open(self.file_storage._FileStorage__file_path, "r") as f:
            data = json.load(f)
        self.assertIn("BaseModel." + self.base_model.id, data)

    def test_reload(self):
        """
        Test the reload method of FileStorage.
        """
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        self.file_storage.reload()
        all_objs = self.file_storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 2)
