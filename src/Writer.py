
from Book import Book


class Writer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []
    
    def add_book_published(self, book: Book):
        self.books.append(book)
    
