from Publisher import Publisher
from Writer import Writer

class Product:
    def get_type(self):
        return self.type
    

class Book(Product):
    def __init__(self, title: str, gender:str, writer: Writer , edition: int, publisher: Publisher, buy_price: float, sell_price:float, tax_ratio: float) -> None:
        self.type = "book"
        self.title = title
        self.gender = gender
        self.writer = writer
        self.edition = edition
        self.publisher = publisher
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.tax_ratio = tax_ratio

    def get_taxes(self):
        return (self.sell_price - self.buy_price)*self.tax_ratio

