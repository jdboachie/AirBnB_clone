import datetime
import unittest
from uuid import uuid4

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test the __init__ method"""
        model = BaseModel()
        # self.assertAlmostEquals(model.id, uuid4())
        self.assertIsInstance(datetime.datetime.strptime(model.created_at,
                                                         "%Y-%m-%dT%H:%M:%S.%f"),
                              datetime.datetime)
        self.assertIsInstance(datetime.datetime.strptime(model.updated_at,
                                                         "%Y-%m-%dT%H:%M:%S.%f"),
                              datetime.datetime)

    def test_str(self):
        """Test the __str__ method"""
        model = BaseModel()
        expected_str = f"[{model.__class__.__name__}] ({model.id}) <{model.__dict__}>"
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Test the save method"""
        model = BaseModel()
        model.save()
        self.assertGreaterEqual(model.updated_at, model.created_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model = BaseModel()
        expected_dict = model.__dict__.copy()
        expected_dict["__class__"] = model.__class__.__name__
        self.assertEqual(model.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
