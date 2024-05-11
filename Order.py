class Order:
    def __init__(self, id = None, date = None, employee = None, client = None, productList = None, totalPrice = None, stock = None, supplier = None):
        self.id = id
        self.date = date
        self.employee = employee
        self.client = client
        self.productList = productList
        self.totalPrice = totalPrice
        self.stock = stock
        self.supplier = supplier
        
    def __str__(self):
        return f"Order ID: {self.id}\nDate: {self.date}\nEmployee: {self.employee}\nClient: {self.client}\nProduct List: {self.productList}\nTotal Price: {self.totalPrice}\nStock: {self.stock}\nSupplier: {self.supplier}"