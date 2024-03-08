from entity.Products import Products
from exception.ProductNotFoundException import ProductNotFoundException

class ProductsDAO(Products):
    def __init__(self):
        super().__init__()

    def perform_Product_actions(self):
        while True:
            print("(Products) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.create_products_table()
            elif ch == 2:
                print(self.add_products())
            elif ch == 3:
                print(self.update_products())
            elif ch == 4:
                print(self.delete_products())
            elif ch == 5:
                print(self.select_products())
            elif ch == 0:
                break
            else:
                print("Invalid input")

    def create_products_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Products(
                            productId INT PRIMARY KEY,
                            name VARCHAR(50) NOT NULL,
                            price FLOAT,
                            description TEXT,
                            stockQuantity INT NOT NULL
                            )
                            '''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("Products Table created successfully")
        except Exception as e:
            print(e)

    def add_products(self):
        try:
            self.open()
            self.productId = int(input("Enter Product ID: "))
            self.name = input("Enter Name: ")
            self.price = float(input("Enter price: "))
            self.description = input("Enter description about product: ")
            self.stockQuantity = int(input("Enter stock Quantity: "))
            data = [(self.productId,self.name,self.price,self.description,self.stockQuantity)]
            insert_str = '''INSERT INTO Products(productId,name,price,description,stockQuantity)
                            VALUES(%s,%s,%s,%s,%s)'''

            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            self.close()
            print("Inserted Successfully")
            return True
        except Exception as e:
            print(e)

    def update_products(self):
        try:
            self.open()
            product_id = int(input("Enter Product ID to be updated: "))
            self.name = input("Enter name: ")
            self.price = float(input("Enter price: "))
            self.description = input("Enter description: ")
            self.stockQuantity = int(input("Enter stock quantity: "))
            data = [(self.name,self.price,self.description,self.stockQuantity,product_id)]
            update_str = f'''UPDATE Products SET name = %s, price = %s, description = %s, stockQuantity = %s
                            WHERE productId = %s'''
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            self.close()
            print("Updated Successfully")
            return True
        except ProductNotFoundException as e:
            return e

    def delete_products(self):
        try:
            self.open()
            product_id = int(input("Enter productId to be deleted: "))
            delete_str = f'''DELETE FROM Products WHERE productId = {product_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            print("Deleted Successfully")
            return True
        except ProductNotFoundException as e:
            return e

    def select_products(self):
        try:
            self.open()
            select_str = '''SELECT * FROM Products'''
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            for i in records:
                print(i)
        except Exception as e:
            print(e)

