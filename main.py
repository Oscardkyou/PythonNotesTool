from notes.manager import NotesManager

def display_commands():
    """Отображает список доступных команд."""
    commands = """
    Доступные команды:
    - add               : добавить новую заметку
    - list              : отобразить список всех заметок
    - view <ID>         : просмотреть заметку по ID
    - edit <ID>         : редактировать заметку по ID
    - delete <ID>       : удалить заметку по ID
    - exit или quit     : выйти из приложения
    """
    print(commands)

def main():
    manager = NotesManager()

    while True:
        command = input("Введите команду (или 'help' для просмотра команд): ")

        if command == 'help':
            display_commands()
        elif command == 'add':
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            note = manager.add(title, body)
            print(f"Заметка с ID {note.id} успешно сохранена.")
        elif command == 'list':
            notes = manager.get_all()
            for note in notes:
                print(f"{note.id}. {note.title} - {note.body[:50]}...")
        elif command.startswith('view '):
            _, note_id_str = command.split()
            note_id = int(note_id_str)
            note = manager.get_by_id(note_id)
            if note:
                print(f"Заметка {note.id}: {note.title} - {note.body}")
            else:
                print(f"Заметка с ID {note_id} не найдена.")
        elif command.startswith('edit '):
            _, note_id_str = command.split()
            note_id = int(note_id_str)
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            edited_note = manager.update(note_id, title, body)
            if edited_note:
                print("Заметка успешно отредактирована.")
            else:
                print(f"Заметка с ID {note_id} не найдена.")
        elif command.startswith('delete '):
            _, note_id_str = command.split()
            note_id = int(note_id_str)
            message = manager.delete(note_id)
            print(message)
        elif command in ['exit', 'quit']:
            break
        else:
            print("Неизвестная команда. Введите 'help' для просмотра доступных команд.")

if __name__ == "__main__":
    main()
