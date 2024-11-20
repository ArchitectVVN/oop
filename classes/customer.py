class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Customer(name='{self.name}', orders={len(self.orders)})"

    def __repr__(self):
        return self.__str__()
