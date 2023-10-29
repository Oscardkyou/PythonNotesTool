# models.py

from datetime import datetime

class Note:
    def __init__(self, identifier, title, body, timestamp=None):
        self.id = identifier
        self.title = title
        self.body = body
        self.timestamp = timestamp if timestamp else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
