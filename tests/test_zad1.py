import unittest
from unittest.mock import patch, mock_open
from src.zad1 import File


class TestFile(unittest.TestCase):

    def test_read(self):
        file = "Lorem ipsum dolor sit amet"
        path = "file.txt"
        with patch('builtins.open', mock_open(read_data=file)):
            self.assertEqual(["Lorem ipsum dolor sit amet"], self.file.read(path))

    def setUp(self):
        self.file = File()

    def tearDown(self) -> None:
        self.file = None
