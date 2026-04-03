# class Vehicles:
#
#     def __init__(self, brand):
#         self.brand = brand
#
#     def drive(self):
#         print(f'Машина {self.brand} едет')
#
#
# class Car(Vehicles):
#
#     def open_trunk(self):
#         print('Багажник открыт')
#
#
# car = Car('bmw')
# car.drive()
# car.open_trunk()

# Задание 1: Магазин книг

# class Bookstore:
#     books_count = 0
#
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#         Bookstore.books_count += 1
#
#     def get_info(self):
#         return f'Книга {self.title} стоит {self.price}'
#
#     @classmethod
#     def total_books(cls):
#         print(f'Всего книг {cls.books_count}')
#
#     @classmethod
#     def from_string(cls, book):
#         title, price = book.split(',')
#         return cls(title.strip(), price.strip())
#
#     @staticmethod
#     def is_valid_price(price):
#         return price > 0
#
# book1 = Bookstore('Гарри Поттер', 500)
# book2 = Bookstore.from_string('Властелин колец,600')
#
# print(book1.get_info())
# Bookstore.total_books()
# print(Bookstore.is_valid_price(-10))

# Задание 2: Банковский счет
#
# class BankAccount:
#     bank_name = 'xdd'
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if self.is_amount_valid(amount):
#             self.balance += amount
#             return f'{self.owner} пополнил счет на {amount}. Баланс: {self.balance}'
#         return 'Сумма должна быть больше 0'
#
#     def withdraw(self, amount):
#         if not self.is_amount_valid(amount):
#             return 'Сумма должна быть больше 0'
#         elif self.balance > amount:
#             self.balance -= amount
#             return f'{self.owner} снял {amount}. Баланс: {self.balance}'
#         return 'Недостаточно средств'
#
#     @classmethod
#     def bank_info(cls):
#         return f'Добро пожаловать в {cls.bank_name}'
#
#     @staticmethod
#     def is_amount_valid(amount):
#         return amount > 0
#
#
# acc1 = BankAccount('Анна', 1000)
# print(acc1.bank_info())
# print(acc1.deposit(500))
# print(acc1.deposit(-500))
# print(acc1.withdraw(2000))
# print(acc1.withdraw(-2000))
# print(acc1.withdraw(700))
#
# print(BankAccount.is_amount_valid(-50))

# Задание 3: Проверка паролей
# import re
# class User:
#
#     def __init__(self, username):
#         self.username = username
#
#     def set_password(self, password):
#         is_valid, error = self.is_password_valid(password)
#         if is_valid:
#             self.password = password
#             return 'Пароль сохранен'
#         return error
#
#     @staticmethod
#     def is_password_valid(password: str):
#         pattern = '[0-9]'
#         if len(password) < 6:
#             return False, 'Пароль должен быть длиннее 6 символов'
#         elif not re.search(pattern, password):
#             return False, 'Пароль должен содержать хотя бы 1 цифру'
#         return True, None
#
#
# user = User('peepo')
# print(user.set_password('qweasds'))
# print(user.set_password('qwe5asd'))
# print(user.set_password('qweas'))
# print(user.set_password('1qweas'))
# print(user.is_password_valid('asd@asd#1'))
# print(user.username, user.password)

# Задание 3: Калькулятор

# class Calculator:
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
#     @classmethod
#     def description(cls):
#         return 'Это калькулятор'
#
#
# print(Calculator.add(3, 5))
# print(Calculator.multiply(4, 6))
# print(Calculator.description())