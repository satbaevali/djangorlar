import os

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"Title: {self.title}")
        print(f"Content:\n{self.content}")
        print("-" * 30)

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

def demo_notes():
    manager = NotesManager()
    note1 = Note("Todo", "Finish Git practice today")
    note2 = Note("Idea", "Build a Django app with user login")
    manager.save(note1)
    manager.save(note2)
    print("Saved notes.")
    print("\nLoaded notes:")
    for note in manager.load_all():
        note.display()

if __name__ == "__main__":
    demo_notes()
