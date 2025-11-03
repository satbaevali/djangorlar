import os

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"[{self.title.upper()}]")
        print(self.content)
        print("-" * 35)

class NotesManager:
    def __init__(self, filename="notes.txt"):
        self.filename = filename

    def save(self, note):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{note.title}:{note.content}\n")

    def load_all(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        notes = []
        for line in lines:
            if ":" in line:
                title, content = line.strip().split(":", 1)
                notes.append(Note(title, content))
        return notes

    def delete_all(self):
        open(self.filename, "w").close()
        print("All notes deleted!")

def demo_notes():
    manager = NotesManager()
    manager.save(Note("Task", "Complete duplicate-4 branch"))
    manager.save(Note("Reminder", "Push changes to GitHub"))
    print("Duplicate-4 notes demo:")
    print("\nAll notes:")
    for note in manager.load_all():
        note.display()
    manager.delete_all()

if __name__ == "__main__":
    demo_notes()
