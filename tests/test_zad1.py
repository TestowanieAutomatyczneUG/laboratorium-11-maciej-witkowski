import unittest
from unittest.mock import patch, mock_open
from unittest import mock
from pathlib import Path
from src.zad1 import File


class TestFile(unittest.TestCase):

    def test_read(self):
        file = "Lorem ipsum dolor sit amet"
        path = "./mock/file.txt"
        open_mock = mock_open(read_data=file)

        with patch('builtins.open', open_mock):
            self.assertEqual(["Lorem ipsum dolor sit amet"], self.file.read(path))

        open_mock.assert_called_once_with(path, 'r')

    def test_write(self):
        content = "Lorem ipsum dolor sit amet"
        path = "./mock/file2.txt"
        open_mock = mock_open()

        with patch('builtins.open', open_mock):
            self.file.write(path, content)

        open_mock.assert_called_once_with(path, 'w')
        open_mock().write.assert_called_once_with("Lorem ipsum dolor sit amet")

    @mock.patch('src.zad1.Path')
    def test_delete_file_exists(self, mock_Path):
        path = "./mock/file_to_delete.txt"
        mock_Path(path).exists.return_value = True

        self.file.delete(path)
        mock_Path(path).unlink.assert_called_with()

    @mock.patch('src.zad1.Path')
    def test_delete_file_doesnt_exists(self, mock_Path):
        path = "./mock/file_to_delete.txt"
        mock_Path(path).exists.return_value = False

        self.assertRaises(FileExistsError, self.file.delete, path)

    def setUp(self):
        self.file = File()

    def tearDown(self) -> None:
        self.file = None
