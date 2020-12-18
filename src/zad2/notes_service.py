from zad2.notes_storage import NotesStorage


class NotesService:

    def __init__(self):
        self.notes = NotesStorage()

    def add(self, note):
        if not hasattr(note, 'name') or not hasattr(note, 'note'):
            raise TypeError("Input has to be object of Note class")

        self.notes.add(note)
        return self.notes

    def averageOf(self, name):
        allNotes = self.notes.get_all_notes_of(name)

        if not allNotes:
            raise Exception("This student has no grades!")

        return sum(x.note for x in allNotes) / len(allNotes)

    def clear(self):
        self.notes.clear()
