# def add(a, b):
#     return a+b
# print(add(3, 5))

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(6))
# print(is_even(9))

# def power(x, exp=2):
#     return x ** exp
# print(power(3))
# print(power(2, 3))

# def max_of_three(a, b, c):
#     return max(a, b, c)
# print(max_of_three(4, 9, 1))

def squares(nums):
    new_lst = []
    for num in nums:
        num **= 2
        new_lst.append(num)
    return new_lst
    return [num ** 2 for num in nums]
print(squares([1, 2, 3]))
