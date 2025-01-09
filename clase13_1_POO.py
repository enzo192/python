
#----------------------clase persona----------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        

person1 = Person("Enzo", 32)
person2 = Person("Lucas", 25)

person1.greet()
person2.greet()


#------------------------clase cuanta de banco------------------------
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:    
            print("Account is not active.")
            
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Account is not active.")
            
    
    def deactivate_account(self):
        self.is_active = False
        print("Account closed.")
        
    def activate_account(self):
        self.is_active = True
        print("Account activated.")
        
        
account1 = BankAccount("Enzo", 1000)
account2 = BankAccount("Lucas", 500)

#llamadas a los métodos
account1.deposit(500)
account2.deposit(1000)
account1.deactivate_account()
account1.deposit(1000)
account1.activate_account()
account1.deposit(1000)
        


#---------------------clase biblioteca---------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed.")
        else:
            print(f"{self.title} is not available.")
            
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} returned.")
        else:
            print(f"{self.title} is already available.")
    

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.books_borrowed = []
        
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.books_borrowed.append(book)
        else:
            print(f"Book is not available.")
            
    def return_book(self, book):
        if book in self.books_borrowed:
            book.return_book()
            self.books_borrowed.remove(book)
        else:
            print(f"You have not borrowed this book.")
    
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to library.")
        
    def add_user(self, user):
        self.users.append(user)
        print(f"{user.name} added to library.")
        
    def display_books(self):
        print("Books in library:")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")
            
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"Book not found.")
                       
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
        
#crear libros    
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("The Catcher in the Rye", "J.D. Salinger")
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald")

#crear usuarios
user1 = User("Enzo", 1)

#crear biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_user(user1)

#mostrar libros
library.display_books()

#prestar libro
user1.borrow_book(book1)

#mostrar libros
library.display_books()

#devolver libro
user1.return_book(book1)

#mostrar libros
library.display_books()
