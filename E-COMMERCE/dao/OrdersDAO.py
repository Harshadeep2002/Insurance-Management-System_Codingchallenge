from entity.Orders import Orders
from exception.OrderNotFoundException import OrderNotFoundException
class OrdersDAO(Orders):
    def __init__(self):
        super().__init__()

    def perform_Orders_actions(self):
        while True:
            print("(Orders) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.create_Orders_table()
            elif ch == 2:
                print(self.add_Orders())
            elif ch == 3:
                print(self.update_Orders())
            elif ch == 4:
                print(self.delete_Orders())
            elif ch == 5:
                print(self.select_Orders())
            elif ch == 0:
                break
            else:
                print("Invalid input")

    def create_Orders_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Orders(
                            orderId INT PRIMARY KEY,
                            customerId INT,
                            orderDate DATE,
                            totalPrice FLOAT,
                            shippingAddress VARCHAR(50),
                            FOREIGN KEY(customerId) REFERENCES Customers(CustomerId) ON DELETE CASCADE
                            )
                            '''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("Orders Table created successfully")
        except Exception as e:
            print(e)

    def add_Orders(self):
        try:
            self.open()
            self.orderId = int(input("Enter Order ID: "))
            self.customerId = int(input("Enter Customer ID: "))
            self.orderDate = input("Enter Order date: ")
            self.totalPrice = float(input("Enter Total Price: "))
            self.shippingAddress = input("Enter Shipping Address: ")
            data = [(self.orderId,self.customerId,self.orderDate,self.totalPrice,self.shippingAddress)]
            insert_str = '''INSERT INTO Orders(orderId,customerId,orderDate,totalPrice,shippingAddress)
                            VALUES(%s,%s,%s,%s,%s)'''

            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            self.close()
            print("Inserted Successfully")
            return True
        except Exception as e:
            print(e)

    def update_Orders(self):
        try:
            self.open()
            order_id = int(input("Enter Order ID to be updated: "))
            self.customerId = int(input("Enter Customer ID: "))
            self.orderDate = input("Enter Order Date: ")
            self.totalPrice = float(input("Enter Total Price: "))
            self.shippingAddress = input("Enter Shipping Address: ")
            data = [(self.customerId,self.orderDate,self.totalPrice,self.shippingAddress,order_id)]
            update_str = f'''UPDATE Orders SET customerId = %s, orderDate = %s, totalPrice = %s, shippingAddress = %s
                            WHERE orderId = %s'''
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            self.close()
            print("Updated Successfully")
            return True
        except OrderNotFoundException as e:
            return 3

    def delete_Orders(self):
        try:
            self.open()
            order_id = int(input("Enter Order Id to be deleted: "))
            delete_str = f'''DELETE FROM Orders WHERE orderId = {order_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            print("Deleted Successfully")
            return True
        except OrderNotFoundException as e:
            return e

    def select_Orders(self):
        try:
            self.open()
            select_str = '''SELECT * FROM Orders'''
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            for i in records:
                print(i)
        except Exception as e:
            print(e)


