from abc import ABC, abstractmethod

class IProductBuilder(ABC):
    @abstractmethod
    def set_id(self,id):
        pass
    @abstractmethod
    def set_name(self, name):
        pass
    @abstractmethod
    def set_description(self, description):
        pass
    @abstractmethod
    def set_price(self, price):
        pass
    @abstractmethod
    def set_stock(self, stock):
        pass
    @abstractmethod
    def build(self):
        pass
