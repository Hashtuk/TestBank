# numbers = [1, 4, 7, 10, 13, 16, 19]
#
# new_number = numbers[1::2]
#
# print(new_number)
#
#
# lst = [1, 2, 3, 4, 5]
#
# def lst_backwards(lst: list) -> list:
#     return lst[::-1]
#
# print(lst_backwards(lst))
# print(lst)
import time


# Проверка на полиндром

# def is_palindrome(word: str) -> bool:
#     return word == word[::-1]
#
#
# print(is_palindrome(word="шалаш"))


# Числа Фибоначчи

# def sum_of_nums(n: int) -> int:
#     next_num = 1
#     num = 0
#     summ = 1
#     stop = 0
#     while stop < n:
#         next_num += num
#         num = next_num - num
#         summ += next_num
#         stop = next_num + num
#     return summ
#
# def sum_of_nums_2(n: int) -> int:
#     a, b = 1, 1
#     summ = 0
#     while a < n:
#         summ += a
#         a, b = b, a+b
#     return summ
#
# print(sum_of_nums(100))
# print(sum_of_nums_2(100))

# Сумма и среднее четных чисел в списке

# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # lst = [1, 3, 5, 2, 0]
# even_lst = [num for num in lst if num % 2 == 0]
# if even_lst != []:
#     even_sum = sum(even_lst)
#     avg_sum = sum(even_lst) / len(even_lst)
#     print(even_sum)
#     print(avg_sum)
# else:
#     print("Четных чисел нет")


