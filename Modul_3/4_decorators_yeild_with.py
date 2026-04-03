# Логирующий декоратор log_calls
#
# def log_calls(func):
#     def wrapper(*args, **kwargs):
#         print(f'Вызвана функция {func.__name__}')
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log_calls
# def some_function():
#     print('Hi')
#
#
# some_function()

# setter, getter

# class Users:
#
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, new_username):
#         self.__username = new_username
#
# user = Users('abc', 123)
# print(user.username)
# user.username = 23423423423
# print(user.username)

# Генератор
# def even_numbers(n):
#     # num = 0
#     # while num <= n:
#     #     if num % 2 == 0:
#     #         yield num
#     #     num += 1
#     for num in range(0, n + 1, 2):
#         yield num
#
# even = even_numbers(10)
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))
# even2 = even_numbers(10)
# print([n for n in even2])
# print([n for n in even2])
# print([n for n in even_numbers(10)])

# Контекстный менеджер
# from contextlib import contextmanager
# @contextmanager
# def simple_counter():
#     print('Начало блока')
#     yield
#     print('Конец блока')
#
# with simple_counter():
#     print('123')