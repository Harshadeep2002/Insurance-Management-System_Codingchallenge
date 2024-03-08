from entity.Customers import Customers
from entity.Products import Products

class Cart(Customers,Products):
    def __init__(self):
        super().__init__()
        self.cartId = 0
        self.customerId = 0
        self.productId = 0
        self.quantity = 0

    #Setters

    def set_cartId(self,value):
        self.cartId = value

    def set_customerId(self,value):
        self.customerId = value

    def set_productId(self,value):
        self.productId = value

    def set_quantity(self,value):
        self.quantity = value

    #Getters

    def get_cartId(self):
        return self.cartId

    def get_customerId(self):
        return self.customerId

    def get_productId(self):
        return self.productId

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f'cartId : {self.cartId} customerId: {self.customerId}\n' \
                f'productId : {self.productId} quantity: {self.quantity}')