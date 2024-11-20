class Discount:
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(amount: float, discount_percent: float) -> float:
        return amount * (1 - discount_percent / 100)

    @staticmethod
    def seasonal_discount(amount: float) -> float:
        # Пример сезонной скидки 10%
        return Discount.apply_discount(amount, 10)

    @staticmethod
    def promo_code_discount(amount: float, promo_code: str) -> float:
        # Пример: промокод 'SAVE20' дает 20% скидку
        if promo_code == 'SAVE20':
            return Discount.apply_discount(amount, 20)
        return amount

    def __str__(self):
        return f"Discount(description='{self.description}', discount_percent={self.discount_percent}%)"

    def __repr__(self):
        return self.__str__()
