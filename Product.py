class Product:

    def __init__(self, id=None, name=None, description=None,price=None, stock=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price}, Stock: {self.stock}"