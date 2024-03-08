class OrderNotFoundException(Exception):
    def __init__(self,orderId):
        super(). __init__(f'Order ID: {orderId} not found in the system..')