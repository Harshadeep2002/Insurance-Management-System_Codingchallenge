from dao.ProductsDAO import ProductsDAO
from dao.OrdersDAO import OrdersDAO
from dao.OrderItemsDAO import OrderItemsDAO
from dao.CustomersDAO import CustomerDAO
from dao.CartDAO import CartDAO
from exception.OrderNotFoundException import OrderNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException
from exception.CustomerNotFoundException import CustomerNotFoundException
from util.DBConnUtil import DBConnection
from dao.OrderProcessor import OrderProcessor

def main():
    dbconnection = DBConnection()

    try:
        dbconnection.open()
        print("--Database Is Connected:--")
    except Exception as e:
        print(e)

    try:
        print("=" * 22)
        print("E-Commerce Application")
        print("=" * 22)
        print("Welcome to E commerce Online Shopping!")

        while True:
            print("1.Customer 2.Products 3.Cart 4.Orders 5.Order Items 0.exit")
            ch = int(input("Enter choice: "))
            if ch == 1:
                c = CustomerDAO()
                c.perform_customer_actions()
            elif ch == 2:
                p = ProductsDAO()
                p.perform_Product_actions()
            elif ch == 3:
                c1 = CartDAO()
                c1.perform_cart_actions()
            elif ch == 4:
                o = OrdersDAO()
                o.perform_Orders_actions()
            elif ch == 5:
                o1 = OrderItemsDAO()
                o1.perform_OrderItems_actions()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

        ecommerce = OrderProcessor()

        while True:
            print("*"*10)
            print("---Menu---")
            print("*"*10)
            print("1.Register Customer\n2.Create Product\n3.Delete Product\n4.Delete Customer\n5.Add To Cart\n6.Remove From Cart\n7.View Cart\n8.Place Order\n9.View Customer Order\n0.Exit")
            ch = int(input("Enter choice: "))
            if ch == 1:
                print(f'Customer Created {ecommerce.createCustomer()}')
            elif ch == 2:
                ecommerce.createProduct()
            elif ch == 3:
                print(f'Product deleted: {ecommerce.deleteProduct()}')
            elif ch == 4:
                ecommerce.deleteCustomer()
            elif ch == 5:
                ecommerce.addToCart()
            elif ch == 6:
                ecommerce.removefromCart()
            elif ch == 7:
                ecommerce.viewCart()
            elif ch == 8:
                print(f'Order placed : {ecommerce.placeOrder()}')
            elif ch == 9:
                print(f'Customer Orders: {ecommerce.viewCustomerOrder(int(input("Enter customer ID:")))}')
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    except CustomerNotFoundException as e:
        return e
    except ProductNotFoundException as e:
        return e
    except OrderNotFoundException as e:
        return e

    finally:
        dbconnection.close()
        print("Thank you for visiting!!")
        print("--Connection is closed__")

if __name__ == "__main__":
    main()



