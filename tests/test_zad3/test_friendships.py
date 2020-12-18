import unittest
from zad3.friendships import FriendShips


class TestFriendShips(unittest.TestCase):

    def test_addFriend_new_person(self):
        self.friends.addFriend('Maciej', 'Kamil')
        self.assertEqual(self.friends.friends, {'Maciej': ['Kamil']})

    def test_addFriend_new_friend(self):
        self.friends.friends = {'Maciej': ['Kamil']}
        self.friends.addFriend('Maciej', 'Paweł')
        self.assertEqual(self.friends.friends, {'Maciej': ['Kamil', 'Paweł']})

    def test_makeFriends_new_persons(self):
        self.friends.makeFriends('Maciej', 'Kamil')
        self.assertEqual(self.friends.friends, {
            'Maciej': ['Kamil'],
            'Kamil': ['Maciej']
        })

    def test_makeFriends_one_new_person(self):
        self.friends.friends = {'Kamil': ['Arkadiusz']}
        self.friends.makeFriends('Maciej', 'Kamil')
        self.assertEqual(self.friends.friends, {
            'Kamil': ['Arkadiusz', 'Maciej'],
            'Maciej': ['Kamil']
        })

    def test_getFriendsList_person_exists(self):
        self.friends.friends = {'Kamil': ['Arkadiusz', 'Maciej']}
        self.assertEqual(self.friends.getFriendsList('Kamil'), ['Arkadiusz', 'Maciej'])

    def test_getFriendsList_person_doesnt_exists(self):
        self.assertEqual(self.friends.getFriendsList('Kamil'), False)

    def test_areFriends_true(self):
        self.friends.friends = {
            'Kamil': ['Arkadiusz', 'Maciej'],
            'Maciej': ['Kamil']
        }
        self.assertEqual(self.friends.areFriends('Kamil', 'Maciej'), True)

    def test_areFriends_false_one_wrong(self):
        self.friends.friends = {
            'Kamil': ['Arkadiusz', 'Maciej'],
            'Maciej': ['Arkadiusz']
        }
        self.assertEqual(self.friends.areFriends('Kamil', 'Maciej'), False)

    def test_areFriends_false_no_friends(self):
        self.friends.friends = {
            'Kamil': ['Arkadiusz', 'Tymon'],
            'Maciej': ['Arkadiusz', 'Łukasz']
        }
        self.assertEqual(self.friends.areFriends('Kamil', 'Maciej'), False)

    def test_addFriend_input_not_string(self):
        self.assertRaises(TypeError, self.friends.addFriend, 'Maciej', ['Kamil'])

    def test_addFriend_input_empty(self):
        self.assertRaises(ValueError, self.friends.addFriend, '', 'Kamil')

    def test_addFriend_input_blank(self):
        self.assertRaises(ValueError, self.friends.addFriend, '   ', 'Kamil')

    def setUp(self):
        self.friends = FriendShips()

    def tearDown(self):
        self.friends = None


if __name__ == '__main__':
    unittest.main()
