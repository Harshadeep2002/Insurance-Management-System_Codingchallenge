from entity.Orders import Orders
from entity.Products import Products

class OrderItems(Orders,Products):
    def __init__(self):
        super().__init__()
        self.orderitemId = 0
        self.orderId = 0
        self.productId = 0
        self.quantity = 0

    #Setters

    def set_orderitemId(self,value):
        self.orderitemId = value

    def set_orderId(self,value):
        self.orderId = value

    def set_productId(self,value):
        self.productId = value

    def set_quantity(self,value):
        self.quantity = value

    #Getters

    def get_orderitemId(self):
        return self.orderitemId

    def get_orderId(self):
        return self.orderId

    def get_productId(self):
        return self.productId

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f'orderitemId : {self.orderitemId} orderId: {self.orderId}\n' \
                f'productId : {self.productId} quantity: {self.quantity}')