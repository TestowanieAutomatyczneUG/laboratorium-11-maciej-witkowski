from friendships import FriendShips


class FriendShipsStorage:

    def __init__(self):
        self.storage = FriendShips()

    def addFriend(self, person, friend):
        self.storage.addFriend(person, friend)

    def makeFriends(self, person1, person2):
        self.storage.makeFriends(person1, person2)

    def getFriendsList(self, person):
        return self.storage.getFriendsList(person)

    def areFriends(self, person1, person2):
        return self.storage.areFriends(person1, person2)
