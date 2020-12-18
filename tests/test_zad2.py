import unittest
from unittest.mock import MagicMock
from zad2.notes_service import NotesService
from zad2.notes_storage import NotesStorage
from zad2.note import Note


class TestNotesService(unittest.TestCase):

    def test_notes_exists(self):
        notes_service = NotesService()
        self.assertEqual(notes_service.notes.notes, [])

    def test_add_note(self):
        note = Note("Maciej", 5)
        notes_service = NotesService()
        notes_service.add = MagicMock(return_value=[note])

        self.assertEqual(notes_service.add(note), [note])

    def test_add_note_raise(self):
        notes_service = NotesService()
        notes_service.add = MagicMock(side_effect=TypeError)

        self.assertRaises(TypeError, notes_service.add, {'name': "Marcin", 'note': 5})

    def test_averageOf(self):
        notes_service = NotesService()
        notes_service.averageOf = MagicMock(return_value=4)

        self.assertEqual(notes_service.averageOf("Maciej"), 4)

    def test_averageOf_raise(self):
        notes_service = NotesService()
        notes_service.averageOf = MagicMock(side_effect=Exception)

        self.assertRaises(Exception, notes_service.averageOf, "Marcin")

    def test_clear(self):
        notes_service = NotesService()
        notes_service.notes.get_all_notes_of = MagicMock(return_value=0)

        self.assertEqual(notes_service.notes.get_all_notes_of("Maciej"), 0)


if __name__ == '__main__':
    unittest.main()
