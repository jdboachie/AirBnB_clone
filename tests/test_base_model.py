import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        self.assertEqual(str(self.model), "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__))

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreaterEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_returns_dictionary(self):
        dictionary = self.model.to_dict()
        self.assertIsInstance(dictionary, dict)

    def test_to_dict_contains_all_attributes(self):
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['id'], self.model.id)
        self.assertEqual(dictionary['created_at'], self.model.created_at.isoformat())
        self.assertEqual(dictionary['updated_at'], self.model.updated_at.isoformat())

    def test_to_dict_contains_class_name(self):
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['__class__'], 'BaseModel')

    def test_to_dict_only_contains_instance_attributes(self):
        dictionary = self.model.to_dict()
        self.assertEqual(len(dictionary.keys()), len(self.model.__dict__) + 1)  # +1 for '__class__'

    def test_to_dict_json_serializable(self):
        dictionary = self.model.to_dict()
        json_string = json.dumps(dictionary)
        self.assertIsInstance(json_string, str)


if __name__ == '__main__':
    unittest.main()
