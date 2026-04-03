# numbers = [5, 8, 2, 4, 7]
# print(sum(numbers))
from itertools import count

# fruits = ['яблоко', 'банан', 'груша', 'банан', 'киви']
# [fruits.remove(fruit) for fruit in fruits.copy() if fruit == 'банан']
# print(fruits)
#
# banana_haters = []
# for fruit in fruits:
#     if fruit != 'банан':
#         banana_haters.append(fruit)
# print(banana_haters)

# print([1, 2, 3]*3)
#
# a = [4, 5]
# b = [1, 2, 3]
# c = a+b
# c.sort()
# print(c)

# point = (4, 7)
# x, y = point
# print('x =', x, end=' ')
# print('y =', y)

# a = (1, 2, 3)
# b = (4, 5)
# c = a + b
# print(c)
#
# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple[0], my_tuple[-1])

# my_set = {1, 2, 3}
# my_set.add(2)
# my_set.discard(4)
# print(my_set)

# t = 'abcd'
# print(t.split('c'))

# word = 'программирование'
# print(set(word))

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7}
# print(a.intersection(b))
# print(a & b)

# a = {'яблоко', 'банан', 'груша'}
# b = {'банан', 'киви', 'апельсин'}
# print(a | b)
# print(a.union(b))
# print(a.difference(b))

# students = ['Анна', 'Борис', 'Виктор']
# grades = [5, 4, 3]
# print(dict(zip(students, grades)))

# words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# dct = {}
#
# for word in words:
#     dct[word] = words.count(word)
# print(dct)
#
# dct2 = {}
# for word in words:
#     if word in dct2:
#         dct2[word] += 1
#     else:
#         dct2[word] = 1
# print(dct2)

# person = {"name": "Anna", "age": 30}
# update = {"age": 31, "city": "Moscow"}
# person.update(update)
# print(person)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(lst))
# summ = 0
# for num in lst:
#     summ += num
# print(summ)

# lst = [1, -2, 3, -4, -5, -6, 7, 8, 9, -10]
# print([num for num in lst if num >= 0])
# positive_lst = []
# for num in lst:
#     if num >= 0:
#         positive_lst.append(num)
# print(positive_lst)

# tpl = (1, 2, 'hi', 5, 'ha')
# num = 0
# word = 'h'
# if word in tpl or num in tpl:
#     print(True)
# else: print(False)

# tpl1 = (1, 2, 3)
# tpl2 = (3, 4, 5, 6)
#
# print(tpl1+tpl2)

# lst = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9]
# print(set(lst))

# sett1 = {1, 2, 3, 4}
# sett2 = {3, 4, 5, 6}
#
# print(sett1.intersection(sett2))
# print(sett1 & sett2)
# print(sett1 | sett2)

# lst1 = ['one', 'two', 'three']
# lst2 = [1, 2, 3]
# print(dict(zip(lst1, lst2)))

dct1 = {"q": 1, "w": 2, "e": 3}
dct2 = {"w": 4, "r": 5, "t": 6}
dct1.update(dct2)
print(dct1)