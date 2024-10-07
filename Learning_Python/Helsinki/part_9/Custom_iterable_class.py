class Book:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return f"{self.name}" 
        
        
class Bookshelf:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def __iter__(self):
        self.n = 0
        return self #This returns the instance itself as the iterator object.
        
    def __next__(self):
        if self.n < len(self._books):
            book = self._books[self.n]
            self.n += 1
            return book
        
        else: 
            raise StopIteration

# Usage
shelf = Bookshelf()
shelf.add_book(Book("The Life of Python"))
shelf.add_book(Book("A Good Cup of Java"))

for book in shelf:
    print(book.name)  # Outputs book names

# his is a program covering iterable class.
