class ProductNotFoundException(Exception):
    def __init__(self,productId):
        super(). __init__(f'product ID : {productId} not found in the system..')