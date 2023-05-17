import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

        self.assertIsInstance(self.model.id, str)

        self.assertIsInstance(self.model.created_at, datetime)

        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        self.assertEqual(str(self.model), "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__))

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreaterEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        dictionary = self.model.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['id'], self.model.id)
        self.assertEqual(dictionary['created_at'], self.model.created_at.isoformat())
        self.assertEqual(dictionary['updated_at'], self.model.updated_at.isoformat())
        self.assertEqual(dictionary['__class__'], 'BaseModel')
        self.assertEqual(len(dictionary.keys()), len(self.model.__dict__) + 1)  # +1 for '__class__'
        json_string = json.dumps(dictionary)
        self.assertIsInstance(json_string, str)


if __name__ == '__main__':
    unittest.main()
