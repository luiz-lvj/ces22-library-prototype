
from Book import Book, Product


class ProductSold:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
    
    