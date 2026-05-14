class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
        
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
        return self.count
        
    def remove_entry(self, index):
        del self.entries[index]
        
    def __str__(self):
        return "\n".join(self.entries)


class JournalPersistence:

    def save(self, journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))
            
    def load(self, journal, filename):
        with open(filename, 'r') as file:
            journal.entries = file.readlines()
            
    def load_from_web(self, uri):
        pass
