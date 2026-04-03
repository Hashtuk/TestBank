import math
"""
Методы для работы со строками
"""

#1.
# text = "  Python is FUN  "
# print(text.strip().lower())

#2.
# sentence = 'Я люблю яблоки и груши'
# print(sentence.replace('яблоки', 'бананы'))

#3.
# data = "apple, banana, orange, grape"
# print(data.replace(' ', '').split(','))

#4.
# name = 'Михаил'
# if name.capitalize() == name:
#     print(True)
# else: print(False)
# print(name.istitle())
# print(name.capitalize() == name)

#5.
# text = 'Сегодня отличный день для прогулки'
# print(text.index('отличный'))
# print(text.find('отличный'))

""" 
Методы для работы с числами
"""

#1.
# digit = int(input('Enter a digit: '))
# print(round(math.sqrt(digit), 3))

#2.
# print(math.factorial(7))

#3.
# digit = 3.14159
# print(math.ceil(digit))
# print(math.floor(digit))

#4.
# print(math.radians(90))

#5.
# print(math.log(32, 2))

""" 
f строки
"""

#1.
# name = 'Анна'
# age = 28
# print(f'{name} - {age} лет')

#2.
# a = 5
# b = 3
# print(f"{a} + {b} = {a+b}")

#3.
# pi = 3.14159265
# print(f"{pi:.2f}")