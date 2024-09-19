'''
Requirements:
Create a class called Book:

It should have the following attributes:
title: The title of the book.
author: The author of the book.
available: A boolean attribute that indicates if the book is available for borrowing (default is True).

It should have the following methods:
borrow(): If the book is available, mark it as not available and print a message saying the book has been borrowed. If it's already borrowed, print a message that it’s unavailable.
return_book(): Mark the book as available and print a message saying the book has been returned.
Create a class called Library:

The library should manage multiple books.
It should have the following attribute:
books: A list that stores Book objects.
It should have the following methods:
add_book(book): Adds a Book object to the library's collection.
display_books(): Displays all books in the library, showing their title, author, and availability status.
borrow_book(title): Search for a book by title. If found and available, borrow it. Otherwise, show that it's not available or not found.
return_book(title): Search for a book by title and return it to the library

'''
#Class for book
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You've borrowed '{self.title}' by {self.author}.")
        else:
            print(f"You've borrowed '{self.title}' by {self.author}.")
            
    def book_return(self):
        self.available = True
        print(f"You've returned '{self.title}' by {self.author}.")
        
#Class for library

class Library:
    
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
        print(f"Added'{book.title}' by {book.author} to the library.")
    
    def display_books(self):
        print("Books in the library")
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(f"{book.title} by {book.author} - {status}")
            
    def borrow_book(self,title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"'{title}' not found in the library.")
        
    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                book.book_return()
                return
        print(f"'{title}' not found in the library.")
        
# Practice
# Create some books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Create a library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display books
library.display_books()