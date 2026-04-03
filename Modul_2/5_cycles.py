# summ = 0
# for i in range(1, 11):
#     summ += i
# print(summ)

# num_of_times = 0
# num = 0
#
# while num < 20:
#     num += 3
#     num_of_times += 1
# print(num_of_times)

# lst = [1, 3, 5, 7, 8, 9, 11, 20, 16]
#
# for num in lst:
#     if num % 2 == 0:
#         print(f"Найдено нечетное число: {num}")
#         break
#     print(f"{num} - нечетное")

# lst = [1, 2, -3, 4, -5, 6, 7, -8, -9, 10]
#
# for num in lst:
#     if num < 0:
#         continue
#     print(f'Обрабатываю число: {num}')

# row = 3
# column = 5
#
# for i in range(row):
#     for j in range(1, column + 1):
#         print(j, end=' ')
#     print('')

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f'{i} * {j} = {i*j}')
#     print('---')

# num = 1
# summ = 0
# while summ < 50:
#    summ += num
#    num += 1
# print(summ, num - 1)
#
# num = 1
# summ = 0
# while summ < 50:
#    summ += num
#    if summ > 50:
#        print(summ, num)
#    num += 1

# for num in range(1, 11):
#     if num % 2 != 0:
#         print(num)

n = int(input('Enter a number: '))
divider = 2
if n <= 1:
    print('The number has to be more than 1')
else:
    while divider != n:
        if n % divider == 0:
            print(divider)
            break
        divider += 1
    if divider == n:
        print("it's a simple number")

n = int(input('Enter a number: '))
for divider in range(2, n+1):
    if n % divider == 0 and n != divider:
        print(divider)
        break
    elif n % divider == 0 and n == divider:
        print("it's a simple number")
        break


n = int(input('Enter a number: '))

found = False

for i in range(2, n):
    if n % i == 0:
        print(i)
        found = True
        break
if not found:
    print("it's a simple number")

