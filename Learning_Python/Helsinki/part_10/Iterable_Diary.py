class Diary:
    
    def __init__(self) -> None:
        self.diary = []
    
    def __iter__(self):
        self.n = 0
        return self
    
    def add_entry(self, entry):
        self.diary.append(entry)
        
    def __next__(self):
        if self.n < len(self.diary):
            diary_entry = self.diary[self.n]
            self.n += 1
            return diary_entry
        else: raise StopIteration


diary = Diary()
diary.add_entry("Went to the park.")
diary.add_entry("Had a great lunch.")
diary.add_entry("Learned about iterators in Python.")

for entry in diary:
    print(entry)
