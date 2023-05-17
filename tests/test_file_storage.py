import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        # Check if all() returns an empty dictionary initially
        objects = self.storage.all()
        self.assertEqual(objects, {})

    def test_new(self):
        # Check if new() adds an object to the storage
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn('BaseModel.' + obj.id, objects)

    def test_save_and_reload(self):
        # Check if save() and reload() correctly serialize and deserialize objects
        obj1 = BaseModel()
        obj1.name = "Object 1"
        self.storage.new(obj1)
        self.storage.save()

        # Create a new instance of FileStorage and reload objects from the file
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()

        self.assertEqual(len(objects), 1)
        self.assertIn('BaseModel.' + obj1.id, objects)
        loaded_obj1 = objects['BaseModel.' + obj1.id]
        self.assertEqual(loaded_obj1.id, obj1.id)
        self.assertEqual(loaded_obj1.name, obj1.name)

    def test_reload_nonexistent_file(self):
        # Check if reload() does nothing when the file does not exist
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(objects, {})


if __name__ == '__main__':
    unittest.main()
