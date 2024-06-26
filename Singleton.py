class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls,)
        return cls._instance
    
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)