"""write a class named Book with the attributes name, author, genre and year, along with a constructor 
which assigns initial values to these attributes.
"""

class Book:
    def __init__(self,name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")

""""
write the three classes specified below. Each class should have exactly 
the same names and types of attributes as listed.

Please also include a constructor in each class. 
The constructor should take the initial values of the attributes as its arguments, in the order listed below.

Class Checklist
attribute header (string)
attribute entries (list)

Class Customer
attribute id (string)
attribute balance (float)
attribute discount (integer)

Class Cable
attribute model (string)
attribute length (float)
attribute max_speed (integer)
attribute bidirectional (Boolean)

"""
class checklist:
    def __init__(self, header : str,entries : list):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id: str, balance:float, discount: int):
        self.id = id 
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model: str, length: float, max_speed:int, bidirectonal:bool) -> None:
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectonal

class BankAccount:

    # The constructor
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner
        
# define a function creates a new bank account object and returns it

siva_account = BankAccount(100,"Siva")

def open_account(deposit:int, name:str):
    new_account = BankAccount(deposit, name)
    print(f"Bank account created for {new_account.owner} with balance {new_account.balance}")
    
open_account(100, "Siva")