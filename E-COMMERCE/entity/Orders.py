from entity.Customers import Customers

class Orders(Customers):
    def __init__(self):
        super().__init__()
        self.orderId = 0
        self.customerId = 0
        self.orderDate = ' '
        self.totalPrice = 0.0
        self.shippingAddress = ' '

    #Setters

    def set_orderId(self,value):
        self.orderId = value

    def set_customerId(self,value):
        self.customerId = value

    def set_orderDate(self,value):
        self.orderDate = value

    def set_totalPrice(self,value):
        self.totalPrice = value

    def set_shippingAddress(self,value):
        self.shippingAddress = value


    #Getters

    def get_orderId(self):
        return self.orderId

    def get_customerId(self):
        return self.customerId

    def get_orderDate(self):
        return self.orderDate

    def get_totalPrice(self):
        return self.totalPrice

    def get_shippingAddress(self):
        return self.shippingAddress


    def __str__(self):
        return (f'orderId : {self.orderId} customerId: {self.customerId}\n' \
                f'orderDate : {self.orderDate} totalPrice: {self.totalPrice} shippingAddress : {self.shippingAddress}')