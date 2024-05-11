import IProductBuilder
import Product
import Singleton

class ProductBuilder(Singleton,IProductBuilder):    
    def __init__(self):
        self.product = Product()

    def set_id(self, id):
        self.product.id = id
        return self

    def set_name(self, name):
        self.product.name = name
        return self

    def set_description(self, description):
        self.product.description = description
        return self

    def set_price(self, price):
        self.product.price = price
        return self

    def set_stock(self, stock):
        self.product.stock = stock
        return self

    def build(self):
        return self.product