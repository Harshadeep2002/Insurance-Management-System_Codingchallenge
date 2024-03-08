from entity.Customers import Customers
from entity.Products import Products

class CartDAO(Customers,Products):
    def __init__(self):
        super().__init__()

    def perform_cart_actions(self):
        while True:
            print("(Cart) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.create_cart_table()
            elif ch == 2:
                print(self.add_cart())
            elif ch == 3:
                print(self.update_cart())
            elif ch == 4:
                print(self.delete_cart())
            elif ch == 5:
                print(self.select_cart())
            elif ch == 0:
                break
            else:
                print("Invalid input")

    def create_cart_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Cart(
                            cartId INT PRIMARY KEY,
                            customerId INT,
                            productId INT,
                            quantity INT,
                            FOREIGN KEY(customerId) REFERENCES Customers(customerId) ON DELETE CASCADE,
                            FOREIGN KEY(productId) REFERENCES Products(productId) ON DELETE CASCADE
                            )
                            '''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("Cart Table created successfully")
        except Exception as e:
            print(e)

    def add_cart(self):
        try:
            self.open()
            self.cartId = int(input("Enter Cart ID: "))
            self.customerId = int(input("Enter Customer ID: "))
            self.productId = int(input("Enter Product ID: "))
            self.quantity = int(input("Enter quantity: "))
            data = [(self.cartId,self.customerId,self.productId,self.quantity)]
            insert_str = '''INSERT INTO Cart(cartId,customerId,productId,quantity)
                            VALUES(%s,%s,%s,%s)'''

            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            self.close()
            print("Inserted Successfully")
            return True
        except Exception as e:
            print(e)

    def update_cart(self):
        try:
            self.open()
            cart_id = int(input("Enter cart ID to be updated: "))
            self.customerId = int(input("Enter Customer ID: "))
            self.productId = int(input("Enter Product ID: "))
            self.quantity = int(input("Enter quantity: "))
            data = [(self.customerId,self.productId,self.quantity,cart_id)]
            update_str = f'''UPDATE Cart SET customerId = %s, productId = %s, quantity = %s
                            WHERE cartId = %s'''
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            self.close()
            print("Updated Successfully")
            return True
        except Exception as e:
            print(e)

    def delete_cart(self):
        try:
            self.open()
            cart_id = int(input("Enter Cart ID to be deleted: "))
            delete_str = f'''DELETE FROM Cart WHERE cartId = {cart_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            print("Deleted Successfully")
            return True
        except Exception as e:
            print(e)

    def select_cart(self):
        try:
            self.open()
            select_str = '''SELECT * FROM Cart'''
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            for i in records:
                print(i)
        except Exception as e:
            print(e)

