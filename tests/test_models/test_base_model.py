from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_has_classname(self):
        obj_dict = self.model.to_dict()
        self.assertIn('__class__', obj_dict)

    def test_to_dict_has_created_at(self):
        obj_dict = self.model.to_dict()
        self.assertIn('created_at', obj_dict)

    def test_to_dict_has_updated_at(self):
        obj_dict = self.model.to_dict()
        self.assertIn('updated_at', obj_dict)