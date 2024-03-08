from util.DBConnUtil import DBConnection

class Products(DBConnection):
    def __init__(self):
        super().__init__()
        self.productId = 0
        self.name = ' '
        self.price = 0.0
        self.description = ' '
        self.stockQuantity = 0

    #Setters

    def set_productId(self,value):
        self.productId = value

    def set_name(self,value):
        self.name = value

    def set_price(self,value):
        self.price = value

    def set_description(self,value):
        self.description = value

    def set_stockQuantity(self,value):
        self.stockQuantity = value

    #Getters

    def get_productId(self):
        return self.productId

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def get_stockQuantity(self):
        return self.stockQuantity

    def __str__(self):
        return (f'productId : {self.productId} name: {self.name} price: {self.price}\n' \
                f'description : {self.description} Stock: {self.stockQuantity}')