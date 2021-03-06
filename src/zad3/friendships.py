class FriendShips:

    def __init__(self):
        self.friends = {}

    def addFriend(self, person, friend):
        if not (isinstance(person, str) and isinstance(friend, str)):
            raise TypeError("Inputs must be of string type!")
        if not person or not friend or person.isspace() or friend.isspace():
            raise ValueError("Strings cannot be empty!")

        if person not in self.friends:
            self.friends[person] = [friend]
        else:
            self.friends[person].append(friend)

    def makeFriends(self, person1, person2):
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)

    def getFriendsList(self, person):
        if person in self.friends:
            return self.friends[person]
        else:
            return False

    def areFriends(self, person1, person2):
        if (person1 in self.friends and person2 in self.friends) and (person2 in self.friends[person1] and person1 in self.friends[person2]):
            return True
        else:
            return False
