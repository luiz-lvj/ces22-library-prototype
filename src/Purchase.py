
from Costumer import Costumer


class Purchase:
    def __init__(self, costumer: Costumer):
        self.costumer = costumer
        self.products = []