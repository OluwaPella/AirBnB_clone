#!/usr/bin/python3
"""tests for class file storage"""
import unittest
import os
import json
import inspect
import datetime
import pycodestyle

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_file_storage(unittest.TestCase):
    """ testing the file storage class"""

    @classmethod
    def setUpClass(cls):
        """setting up file storage class"""
        cls.storage = FileStorage()
        try:
            os.rename(FileStorage._FileStorage__file_path, "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """destroying the file storage class"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
            os.rename("test_file.json", FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def test_private_path(self):
        """testing with a private path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_private_dict(self):
        """testing with an instance of a dict"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_with_an_arg(self):
        """testing with an arg"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_with_no_args(self):
        """ testing with no arg"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_all(self):
        """whether it returns a valid dict"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_save(self):
        """testing on adding a new obj"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
if __name__ == "__main__":
    unittest.main()
