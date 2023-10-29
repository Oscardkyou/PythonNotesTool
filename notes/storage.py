# storage.py

import json
from .models import Note

FILE_NAME = 'notes_storage.json'

def load_notes():
    try:
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            return [Note(note['id'], note['title'], note['body'], note['timestamp']) for note in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_notes(notes):
    with open(FILE_NAME, 'w') as file:
        json.dump([note.__dict__ for note in notes], file)
