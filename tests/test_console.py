import unittest
from unittest.mock import patch, MagicMock
from console import HBNBCommand
from models.base_model import BaseModel
from datetime import datetime
import io


class TestHBNBCommandCreate(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.cmd = HBNBCommand()

    @patch('models.storage')
    def test_create_no_class_name(self, mock_storage):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.cmd.do_create("")
            self.assertIn("** class name missing **", mock_stdout.getvalue())

    @patch('models.storage')
    def test_create_invalid_class_name(self, mock_storage):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.cmd.do_create("NonExistentClass")
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('models.storage')
    def test_create_valid_class_no_params(self, mock_storage):
        mock_storage.new = MagicMock()
        mock_storage.save = MagicMock()
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.cmd.do_create("BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Check if an ID was printed

            new_instance = mock_storage.new.call_args[0][0]
            self.assertIsInstance(new_instance, BaseModel)
            self.assertEqual(new_instance.id, output)

    @patch('models.storage')
    def test_create_with_string_param(self, mock_storage):
        mock_storage.new = MagicMock()
        mock_storage.save = MagicMock()
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.cmd.do_create('BaseModel name="My_little_house"')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)
            new_instance = mock_storage.new.call_args[0][0]
            self.assertIsInstance(new_instance, BaseModel)
            self.assertEqual(new_instance.name, "My little house")

    @patch('models.storage')
    def test_create_with_integer_param(self, mock_storage):
        mock_storage.new = MagicMock()
        mock_storage.save = MagicMock()
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.cmd.do_create('BaseModel number=123')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

            new_instance = mock_storage.new.call_args[0][0]
            self.assertIsInstance(new_instance, BaseModel)
            self.assertEqual(new_instance.number, 123)

    @patch('models.storage')
    def test_create_with_float_param(self, mock_storage):
        mock_storage.new = MagicMock()
        mock_storage.save = MagicMock()
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.cmd.do_create('BaseModel number="123.456"')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

            new_instance = mock_storage.new.call_args[0][0]
            self.assertIsInstance(new_instance, BaseModel)
            self.assertEqual(new_instance.number, "123.456")


if __name__ == '__main__':
    unittest.main()
