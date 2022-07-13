from Book import Book
from Costumer import Costumer
from Purchase import Purchase


class Library:
    def __init__(self):
        self.books = []
        self.writers = []
        self.costumers = []
        self.purchases = []
    
    def add_book(self, book: Book):
        if not book in self.books:
            self.books.append(book)
    
    def del_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
    
    def alter_book(self, book: Book, new_book: Book):
        self.del_book(book)
        self.add_book(new_book)
    
    def add_costumer(self, costumer: Costumer):
        if not costumer in self.costumers:
            self.costumers.append(costumer)
    
    def del_costumer(self, costumer: Costumer):
        if costumer in self.costumers:
            self.costumers.remove(costumer)
    
    def alter_costumer(self, costumer: Costumer, new_costumer: Costumer):
        self.del_costumer(costumer)
        self.add_costumer(new_costumer)
        
    def add_purchase(self, purchase: Purchase):
        if not purchase in self.purchases:
            self.purchases.append(purchase)
    
    def del_purchase(self, purchase: Purchase):
        if purchase in self.purchases:
            self.purchases.remove(purchase)
        
    def alter_purchase(self, purchase: Purchase):
        self.del_purchase(purchase)
        self.add_purchase(purchase)
