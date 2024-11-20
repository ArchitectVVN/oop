class Order:
    total_orders = 0
    total_amount = 0.0

    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products
        Order.total_orders += 1
        Order.total_amount += self.get_total()

    def get_total(self):
        return sum(product.price for product in self.products)

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    @classmethod
    def get_total_amount(cls):
        return cls.total_amount

    def __str__(self):
        product_names = ', '.join([product.name for product in self.products])
        return f"Order(products=[{product_names}], total={self.get_total():.2f})"

    def __repr__(self):
        return self.__str__()
