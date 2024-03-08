class CustomerNotFoundException(Exception):
    def __init__(self,customerId):
        super().__init__(f"Customer Id : {customerId} not found in the database")