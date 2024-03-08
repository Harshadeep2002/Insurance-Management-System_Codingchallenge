from dao.CartDAO import CartDAO
from dao.ProductsDAO import ProductsDAO
from dao.CustomersDAO import CustomerDAO
from dao.OrdersDAO import OrdersDAO
from exception.CustomerNotFoundException import CustomerNotFoundException

class OrderProcessor(CartDAO,OrdersDAO):
    def __init__(self):
        super().__init__()

    def createProduct(self):
        p = ProductsDAO()
        p.add_products()

    def createCustomer(self):
        c = CustomerDAO()
        c.add_customers()

    def deleteProduct(self):
        p = ProductsDAO()
        p.select_products()
        print()
        p = ProductsDAO()
        p.delete_products()
        print("After deleting:")
        p = ProductsDAO()
        p.select_products()

    def deleteCustomer(self):
        c = CustomerDAO()
        c.select_customers()
        print()
        c = CustomerDAO()
        c.delete_customers()
        print("After deleting:")
        c = CustomerDAO()
        c.select_customers()

    def addToCart(self):
        c1 = CartDAO()
        c1.add_cart()

    def removefromCart(self):
        c1 = CartDAO()
        c1.select_cart()
        print()
        c1 = CartDAO()
        c1.delete_cart()
        print()

    def viewCart(self):
        print('='*22)
        print("Products for reference")
        print('='*22)
        p1 = ProductsDAO()
        p1.select_products()
        print('-'*13)
        print("items in cart")
        print('-'*13)
        c1 = CartDAO()
        c1.select_cart()
        print()

    def placeOrder(self):
        o = OrdersDAO()
        o.add_Orders()

    def viewCustomerOrder(self,customerId):
        try:
            self.open()
            #customer_id = int(input("Enter customer ID: "))
            self.stmt.execute(f'''SELECT COUNT(*) FROM Orders WHERE customerId = {customerId}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                return CustomerNotFoundException(customerId)
            else:
                print("Total Count or Orders: ", count)
                self.stmt.execute(f'''SELECT * FROM Orders WHERE customerId = {customerId} ''')
                records = self.stmt.fetchall()
                self.close()
                return records

        except CustomerNotFoundException as e:
            return e
        except Exception as e:
            return e

