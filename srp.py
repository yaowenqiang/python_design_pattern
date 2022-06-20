class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def move_entry(self, pos):
        del self.entries[pos]


    def __str__(self):
        return '\n'.join(self.entries)

    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()


    def load(self, filename):
        pass


    def load_from_web(self, uri):
        pass


class PersistenseManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()



j = Journal()

j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries: \n{j}')

filename = 'tmp.txt'
PersistenseManager.save_to_file(j,filename)

with open(filename) as fh:
    print(fh.read())
