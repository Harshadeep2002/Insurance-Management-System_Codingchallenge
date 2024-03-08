from entity.Orders import Orders
from entity.Products import Products

class OrderItemsDAO(Orders,Products):
    def __init__(self):
        super().__init__()

    def perform_OrderItems_actions(self):
        while True:
            print("(Order Items) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.create_OrderItems_table()
            elif ch == 2:
                print(self.add_OrderItems())
            elif ch == 3:
                print(self.update_OrderItems())
            elif ch == 4:
                print(self.delete_OrderItems())
            elif ch == 5:
                print(self.select_OrderItems())
            elif ch == 0:
                break
            else:
                print("Invalid input")

    def create_OrderItems_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS OrderItems(
                            OrderItemId INT PRIMARY KEY,
                            orderId INT,
                            productId INT,
                            quantity INT,
                            FOREIGN KEY(orderId) REFERENCES Orders(orderId) ON DELETE CASCADE,
                            FOREIGN KEY(productId) REFERENCES Products(productId) ON DELETE CASCADE
                            )
                            '''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("OrderItems Table created successfully")
        except Exception as e:
            print(e)

    def add_OrderItems(self):
        try:
            self.open()
            self.OrderItemId = int(input("Enter OrderItem ID: "))
            self.orderId = int(input("Enter order ID: "))
            self.productId = int(input("Enter product ID: "))
            self.quantity = int(input("Enter quantity: "))
            data = [(self.OrderItemId,self.orderId,self.productId,self.quantity)]
            insert_str = '''INSERT INTO OrderItems(OrderItemId,orderId,productId,quantity)
                            VALUES(%s,%s,%s,%s)'''

            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            self.close()
            print("Inserted Successfully")
            return True
        except Exception as e:
            print(e)

    def update_OrderItems(self):
        try:
            self.open()
            OrderItem_id = int(input("Enter OrderItem ID to be updated: "))
            self.orderId = int(input("Enter order ID: "))
            self.productId = int(input("Enter product ID: "))
            self.quantity = int(input("Enter quantity: "))
            data = [(self.orderId,self.productId,self.quantity,OrderItem_id)]
            update_str = f'''UPDATE OrderItems SET orderId = %s, productId = %s, quantity = %s
                            WHERE OrderItemId = %s'''
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            self.close()
            print("Updated Successfully")
            return True
        except Exception as e:
            print(e)

    def delete_OrderItems(self):
        try:
            self.open()
            OrderItem_id = int(input("EnterOrderItem ID to be deleted: "))
            delete_str = f'''DELETE FROM OrderItems WHERE OrderItemId = {OrderItem_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            print("Deleted Successfully")
            return True
        except Exception as e:
            print(e)

    def select_OrderItems(self):
        try:
            self.open()
            select_str = '''SELECT * FROM OrderItems'''
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            for i in records:
                print(i)
        except Exception as e:
            print(e)
