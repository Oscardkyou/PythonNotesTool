from .models import Note
from .storage import load_notes, save_notes

class NotesManager:
    def __init__(self):
        self.notes = {note.id: note for note in load_notes()}

    def add(self, title, body):
        note_id = max(self.notes.keys(), default=0) + 1  # Улучшенный способ генерации ID
        new_note = Note(note_id, title, body)
        self.notes[note_id] = new_note
        save_notes(list(self.notes.values()))
        return new_note

    def delete(self, note_id):
        if note_id in self.notes:
            del self.notes[note_id]
            save_notes(list(self.notes.values()))
            return f"Заметка с ID {note_id} успешно удалена."
        return f"Заметка с ID {note_id} не найдена."

    def update(self, note_id, title=None, body=None):
        if note_id in self.notes:
            if title:
                self.notes[note_id].title = title
            if body:
                self.notes[note_id].body = body
            save_notes(list(self.notes.values()))
            return self.notes[note_id]
        return None

    def get_all(self):
        return list(self.notes.values())

    def get_by_id(self, note_id):
        return self.notes.get(note_id, None)
