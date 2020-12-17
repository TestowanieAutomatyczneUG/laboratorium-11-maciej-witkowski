import unittest
from unittest.mock import patch, mock_open
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

    def setUp(self):
        self.file = File()

    def tearDown(self) -> None:
        self.file = None
