from util.DBConnUtil import DBConnection

class Customers(DBConnection):
    def __init__(self):
        super().__init__()
        self.customerId = 0
        self.name = ' '
        self.email = ' '
        self.password = ' '

    #Setters

    def set_customerId(self,value):
        self.customerId = value

    def set_name(self,value):
        self.name = value

    def set_email(self,value):
        self.email = value

    def set_password(self,value):
        self.password = value

    #Getters

    def get_customerId(self):
        return self.customerId

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def __str__(self):
        return f'customerId : {self.customerId} name: {self.name} email: {self.email} password: {self.password}'