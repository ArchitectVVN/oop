from classes import Product, Customer, Order, Discount

def main():
    # Создание продуктов
    product1 = Product("Ноутбук", 1500.00)
    product2 = Product("Смартфон", 800.00)
    product3 = Product("Наушники", 150.00)
    product4 = Product("Клавиатура", 100.00)

    # Создание клиентов
    customer1 = Customer("Иван Иванов")
    customer2 = Customer("Мария Петрова")

    # Создание заказов
    order1 = Order([product1, product3])  # Ноутбук и Наушники
    order2 = Order([product2])            # Смартфон
    order3 = Order([product4, product4, product3])  # Клавиатура, Клавиатура, Наушники

    # Добавление заказов к клиентам
    customer1.add_order(order1)
    customer1.add_order(order3)

    customer2.add_order(order2)

    # Применение скидок к заказам
    discount1 = Discount("Сезонная скидка", 10)
    discounted_total1 = Discount.seasonal_discount(order1.get_total())
    print(f"Сумма заказа 1 со скидкой: {discounted_total1:.2f} руб.")

    discounted_total2 = Discount.promo_code_discount(order2.get_total(), "SAVE20")
    print(f"Сумма заказа 2 со скидкой: {discounted_total2:.2f} руб.")

    discount3 = Discount("Общая скидка", 5)
    discounted_total3 = Discount.apply_discount(order3.get_total(), discount3.discount_percent)
    print(f"Сумма заказа 3 со скидкой: {discounted_total3:.2f} руб.")

    # Подсчет общего количества заказов и общей суммы
    print(f"\nОбщее количество заказов: {Order.get_total_orders()}")
    print(f"Общая сумма всех заказов: {Order.get_total_amount():.2f} руб.")

    # Вывод информации о продуктах
    print("\nПродукты:")
    print(product1)
    print(product2)
    print(product3)
    print(product4)

    # Вывод информации о клиентах и их заказах
    print("\nКлиенты и их заказы:")
    for customer in [customer1, customer2]:
        print(customer)
        for order in customer.orders:
            print(f"  {order}")

if __name__ == "__main__":
    main()
