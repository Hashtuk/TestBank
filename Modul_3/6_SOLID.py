from abc import ABC, abstractmethod


class Order:
    def __init__(self, items: list, total: int):
        self.items = items
        self.total = total

    def get_info(self):
        print(f'{self.items}. К оплате: {self.total}')


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class CashPayment(PaymentMethod):
    def pay(self, order: Order):
        print(f'Оплата наличными: {order.total} р.')


class CardPayment(PaymentMethod):
    def pay(self, order: Order):
        print(f'Оплата картой: {order.total} р.')


class PaypalPayment(PaymentMethod):
    def pay(self, order: Order):
        print(f'Оплата через PayPal: {order.total} р.')


class OrderProcessor:
    def __init__(self, method: PaymentMethod):
        self.method = method

    def process(self, order: Order):
        print(f'Обрабатываем заказ на сумму {order.total}')
        self.method.pay(order)


o = Order(['Молоко', 'яйца'], 200)
o.get_info()
op = OrderProcessor(CardPayment())
op.process(o)