import unittest
from unittest.mock import MagicMock
from zad3.friendships_storage import FriendShipsStorage


class TestFriendShipsStorage(unittest.TestCase):

    def test_addFriend(self):
        self.storage.storage = MagicMock()
        self.storage.addFriend('Maciej', 'Kamil')
        self.storage.storage.addFriend.assert_called_with('Maciej', 'Kamil')

    def test_makeFriends_new_persons(self):
        self.storage.storage = MagicMock()
        self.storage.makeFriends('Maciej', 'Kamil')
        self.storage.storage.makeFriends.assert_called_with('Maciej', 'Kamil')

    def test_getFriendsList_person_exists(self):
        self.storage.storage.getFriendsList = MagicMock(return_value=['Arkadiusz', 'Maciej'])
        self.assertEqual(self.storage.getFriendsList('Kamil'), ['Arkadiusz', 'Maciej'])

    def test_getFriendsList_person_doesnt_exists(self):
        self.storage.storage.getFriendsList = MagicMock(return_value=False)
        self.assertEqual(self.storage.getFriendsList('Kamil'), False)

    def test_areFriends_true(self):
        self.storage.storage.areFriends = MagicMock(return_value=True)
        self.assertEqual(self.storage.areFriends('Kamil', 'Maciej'), True)
        self.storage.storage.areFriends.assert_called_with('Kamil', 'Maciej')

    def test_areFriends_false(self):
        self.storage.storage.areFriends = MagicMock(return_value=False)
        self.assertEqual(self.storage.areFriends('Maciej', 'Kamil'), False)
        self.storage.storage.areFriends.assert_called_with('Maciej', 'Kamil')

    def test_addFriend_input_not_string(self):
        self.storage.storage.addFriend = MagicMock(side_effect=TypeError)
        self.assertRaises(TypeError, self.storage.addFriend, 'Maciej', ['Kamil'])
        self.storage.storage.addFriend.assert_called_with('Maciej', ['Kamil'])

    def test_addFriend_input_empty(self):
        self.storage.storage.addFriend = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.storage.addFriend, '', 'Kamil')
        self.storage.storage.addFriend.assert_called_with('', 'Kamil')

    def test_addFriend_input_blank(self):
        self.storage.storage.addFriend = MagicMock(side_effect=ValueError)
        self.assertRaises(ValueError, self.storage.addFriend, '  ', 'Kamil')
        self.storage.storage.addFriend.assert_called_with('  ', 'Kamil')

    def setUp(self):
        self.storage = FriendShipsStorage()

    def tearDown(self):
        self.storage = None


if __name__ == '__main__':
    unittest.main()