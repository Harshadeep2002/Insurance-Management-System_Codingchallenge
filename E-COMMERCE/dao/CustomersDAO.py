from entity.Customers import Customers
from exception.CustomerNotFoundException import CustomerNotFoundException

class CustomerDAO(Customers):
    def __init__(self):
        super().__init__()

    def perform_customer_actions(self):
        while True:
            print("(Customers) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.create_customers_table()
            elif ch == 2:
                print(self.add_customers())
            elif ch == 3:
                print(self.update_customers())
            elif ch == 4:
                print(self.delete_customers())
            elif ch == 5:
                print(self.select_customers())
            elif ch == 0:
                break
            else:
                print("Invalid input")

    def create_customers_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Customers(
                            customerId INT PRIMARY KEY,
                            name VARCHAR(50) NOT NULL,
                            email VARCHAR(50),
                            password VARCHAR(50)
                            )
                            '''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("Customers Table created successfully")
        except Exception as e:
            print(e)

    def add_customers(self):
        try:
            self.open()
            self.customerId = int(input("Enter Customer ID: "))
            self.name = input("Enter Name: ")
            self.email = input("Enter Email: ")
            self.password = input("Enter password: ")
            data = [(self.customerId,self.name,self.email,self.password)]
            insert_str = '''INSERT INTO Customers(customerId,name,email,password)
                            VALUES(%s,%s,%s,%s)'''

            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            self.close()
            print("Inserted Successfully")
            return True
        except Exception as e:
            return e

    def update_customers(self):
        try:
            self.open()
            customer_id = int(input("Enter Customer ID to be updated: "))
            self.name = input("Enter name: ")
            self.email = input("Enter Email: ")
            self.password = input("Enter password: ")
            data = [(self.name,self.email,self.password,customer_id)]
            update_str = f'''UPDATE Customers SET name = %s, email = %s, password = %s
                            WHERE customerId = %s'''
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            self.close()
            print("Updated Successfully")
            return True
        except CustomerNotFoundException as e:
            return e

    def delete_customers(self):
        try:
            self.open()
            customer_id = int(input("Enter customerId to be deleted: "))
            delete_str = f'''DELETE FROM Customers WHERE CustomerId = {customer_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            print("Deleted Successfully")
            return True
        except CustomerNotFoundException as e:
            return e

    def select_customers(self):
        try:
            self.open()
            select_str = '''SELECT * FROM Customers'''
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            for i in records:
                print(i)
        except Exception as e:
            print(e)

