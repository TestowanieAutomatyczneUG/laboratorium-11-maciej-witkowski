class Note:

    def __init__(self, name, note):
        if not isinstance(name, str) or not name:
            raise TypeError("Name cannot be null!")

        if not (isinstance(note, int) or isinstance(note, float)):
            raise TypeError("Note cannot be null!")

        if note > 6 or note < 2:
            raise ValueError("Note must be between 2 and 6!")

        self.name = name
        self.note = note

    def getName(self):
        return self.name

    def getNote(self):
        return self.note
