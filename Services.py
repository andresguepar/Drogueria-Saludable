from Client import Client
from Order import Order
from ProductBuilder import ProductBuilder
from Singleton import Singleton


class Services:

    def __init__(self):
        self.products = []

    def prototype(self):
        prototype_client = Client("1","Pacho","Bonito","123","Miau Avenue","321")

        new_client1 = prototype_client.clone()
        new_client1.id = "3"

        new_client2 = prototype_client.clone()
        new_client2.id = "4"
        new_client2.dni = "321"

        print(new_client1)
        print("\n------------------------------------\n")
        print(new_client2)

    def builder(self):
        productBuilder = ProductBuilder()

        productBuilder.set_id("1")
        productBuilder.set_name("Mentalol")
        productBuilder.set_description("Medicamento natural para el dolor")
        productBuilder.set_price(5.00)
        productBuilder.set_stock(10)

        product = productBuilder.build()

        print(product)

    def singleton(self):

        single = Singleton()

        order1 = Order("1","12/05","1","1","[Limon,Sal,Paprica]",200,"1")
        single.add_order(order1)
        print(order1)