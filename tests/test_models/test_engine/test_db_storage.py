#!/usr/bin/python3
"""Module for testing file storage"""
import unittest
from models.engine.db_storage import DBStorage
import models


class TestDBStorage(unittest.TestCase):
    """Tests for the DBStorage class and its methods."""

    @unittest.skipUnless(models.storage_ob == 'db', "Testing DBStorage only")
    def test_doc_class(self):
        """Test for the presence of class docstring."""
        self.assertIsNotNone(DBStorage.__doc__,
                             "Docstring missing in DBStorage")
        self.assertTrue(len(DBStorage.__doc__) > 0, "Docstring missing")

    def test_doc_init(self):
        """Test for the presence of __init__ method docstring."""
        self.assertIsNotNone(DBStorage.__init__.__doc__,
                             "Docstring missing in __init__")
        self.assertTrue(len(DBStorage.__init__.__doc__) > 0,
                        "Docstring missing")

    def test_doc_all(self):
        """Test for the presence of all method docstring."""
        self.assertIsNotNone(DBStorage.all.__doc__,
                             "Docstring missing in all")
        self.assertTrue(len(DBStorage.all.__doc__) > 0, "Docstring missing")

    def test_doc_new(self):
        """Test for the presence of new method docstring."""
        self.assertIsNotNone(DBStorage.new.__doc__,
                             "Docstring missing in new")
        self.assertTrue(len(DBStorage.new.__doc__) > 0, "Docstring missing")

    def test_doc_save(self):
        """Test for the presence of save method docstring."""
        self.assertIsNotNone(DBStorage.save.__doc__,
                             "Docstring missing in save")
        self.assertTrue(len(DBStorage.save.__doc__) > 0, "Docstring missing")

    def test_doc_delete(self):
        """Test for the presence of delete method docstring."""
        self.assertIsNotNone(DBStorage.delete.__doc__,
                             "Docstring missing in delete")
        self.assertTrue(len(DBStorage.delete.__doc__) > 0, "Docstring missing")

    def test_doc_reload(self):
        """Test for the presence of reload method docstring."""
        self.assertIsNotNone(DBStorage.reload.__doc__,
                             "Docstring missing in reload")
        self.assertTrue(len(DBStorage.reload.__doc__) > 0, "Docstring missing")


if __name__ == "__main__":
    unittest.main()
