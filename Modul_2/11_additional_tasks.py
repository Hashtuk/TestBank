"""
if/else
"""
from dataclasses import replace
from os.path import sep
from shlex import join
from wsgiref.validate import assert_

# 1.
# a = "jfnmdbsdfnsjfqenfdssjdfhsdjlkppppppppppppppppppgggggxxzzzssswwwwwwwwwwwwwwwwwwfgdfxdfg"
# total = {}
# for char in a:
#     if char in total:
#         total[char] += 1
#     else:
#         total[char] = 1
# total_reversed = reversed(total)
# print(max(reversed(total), key=total.get))

# 2.
# """
# #################
# #               #
# # Hello, world! #
# #               #
# #################
# """
# a = 17
# b = 5
# sentence = "Hello, world!"
#
# # Проверка на возможность поместить фразу во введенные границы
# assert a % 2 != 0 and b % 2 != 0 if len(sentence) % 2 != 0 else a % 2 == 0 and b % 2 != 0, "'a' must be even if sentence length is even otherwise both odd; 'b' must always be odd"
# assert a >= len(sentence) + 2 and b >= 3, "'a' has to be more than sentence length or 'b' has to be more than 2"
#
# # Строим прямоугольник вокруг фразы
# for row in range(b):
#     for col in range(a):
#         # Условия, чтобы построить не закрашенный прямоугольник, заданного периметра
#         if (row and col) == 0 or col == a-1 or row == b-1:
#             print('#', end='')
#         # Условия для вычисления середины прямоугольника
#         elif row == ((b+1)/2)-1 and col == (a-len(sentence))/2: # Определяется с какой строки и колонки начинать печатать предложение, чтобы оно было посередине
#             for char in sentence: # Печатаем сообщение
#                 print(char, end='')
#             print(' '*int(((a-len(sentence))/2)-1), end='') # Закрываем # в конце
#             print('#', end='')
#             break # Заканчиваем цикл, чтобы перейти на новую строку
#         else:
#             print(' ', end='')
#     print()
# print(b // 2)
# print(((b+1)/2)-1)

# 3.
# def putting_sentence_in_box(sentence, w, h):
#     assert w >= len(sentence) + 2, 'Width is too short'
#     assert h % 2 != 0, "Height can't be even"
#     assert w % 2 != 0, "Width can't be even"
#
#     left_pudding = (w - len(sentence) - 2) // 2
#     right_pudding = w - len(sentence) - 2 - left_pudding
#     middle_row = (h - 2)//2 # Средний индекс
#
#     print('#'*w)
#     for row in range(h - 2):
#         if row == middle_row:
#             print(f'#{" "*left_pudding}{sentence}{" "*right_pudding}#')
#         else:
#             print(f'#{" "*(w - 2)}#')
#     print('#'*w)
# putting_sentence_in_box('Hello, world!', w = 31, h = 7)

# 4.
# def sum_of_fibonacci(n):
#     # 0 1 1 2 3 5 8 ...
#     prev_num = 0
#     num = 1
#     total = 0
#
#     while prev_num < n:
#         total += prev_num
#         prev_num, num = num, num + prev_num
#     return total
# print(sum_of_fibonacci(30))

# 5.
# def string_reverse(word):
#     lst = [char for char in word]
#     left = 0
#     right = len(word) - 1
#
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
#     return ''.join(lst)
# print(string_reverse("Python"))

# 6.
# num = 2794
# print((num // 10) % 10)
# print(num // 10)
# print(82 // 3**2)
# print(24 // 10)

# print([int(c) for c in input().split()])
# lst1 = [1, 2, 4, 6, 234]
# lst2 = [3, 5, 7, 8, 9, 10, 324234234234, 46457568567967979]
#
# first = 0
# second = 0
# res = []
# while first < len(lst1) and second < len(lst2):
#     if lst1[first] <= lst2[second]:
#         res.append(lst1[first])
#         first += 1
#     else:
#         res.append(lst2[second])
#         second += 1
# res.extend(lst1[first:])
# res.extend(lst2[second:])
#
# print(lst1, lst2, res)
# a = [1, 2]
# b = [1, 2]
# c = b
# print(c is b)
# a = 'abc'
# c = a.split()
# print(a, c)
# b = ['a', 'b', 'c']
# b.remove('b')
# print(b)
# b = [['a', 'b', 'c']]*3
# b[2][2] = 10
# print(b)

# PEP
# 1.
# my_variable = 10
# username = "JohnDoe"
# CONSTANT_VALUE = 3.14
#
# #2.
# if 5 > 2:
#     print("Пять больше двух!")
#     print("Это сообщение тоже внутри if.")
#
# #3.
# x = 5 * 3 + 2
# y = x**2 - 1
# if x > 5 and y < 10:
#     print("Условие выполнено")
#
# #4.
# long_message = ("Это очень длинное приветственное сообщение, которое явно выходит за пределы допустимой длины строки "
#                 "в 79 символов, и его нужно как-то красиво разбить.")
#
# #5.
# import math
# import os
#
#
# def calculate_area(radius):
#     return math.pi * radius ** 2
#
#
# radius = 5
# area = calculate_area(radius)
# print(f"Площадь круга с радиусом {radius} равна {area}")

# Переменные, Print и Input, Sep и End
# 1.
# name = input()
# age = input()
# city = input()
# print('Имя', name, end='; ', sep=': ')
# print('Возраст', age, end='; ', sep=': ')
# print('Город', city, end='.', sep=': ')

# #2.
# print('1', '2', '3', '4', '5', sep='*')
#
# #3.
# name = input()
# surname = input()
# initials = name + ' ' + surname
# print(initials)
# print(f'{name} {surname}')
#
# #4.
# print('Раз', end=', ')
# print('Два', end=', ')
# print('Три')
#
# #5.
# a = int(input())
# b = int(input())
# print(a+b, a-b, a*b, a/b, sep='\n')

# Типы данных
# #1.
# a = input()
# print(a, type(a))
#
# #2.
# rubles = 1000
# exchange_rate = 97.5
# print(int(rubles / exchange_rate))
#
# #3.
# a = 0.1
# b = 0.2
# print(a + b) # Наверное потому что пайтон записывает float значения со своей точностью, а не с которой мы задали
#
# #4.
# age = int(input())
# print(2026 - age)
#
# #5.
# my_list = [1, 2]
# my_list[0] = 10
# my_string = "ab"
# my_string[0] = 'z'
# print(my_list) # список изменился на месте, потому что список изменяемый тип данных
# print(my_string) # ошибка TypeError: 'str' object does not support item assignment. Скорее всего ты хотел показать, что строка останется такой же, даже если мы попытаемся изменить что-то в ней после

# Конструкции if, elif, else
# 1.
# a = int(input())
# print("четное") if a % 2 == 0 else print('нечетное')
#
# #2.
# a = int(input())
# if a < 12:
#     print('Доброе утро!')
# elif 12 <= a <= 17:
#     print('Добрый день!')
# elif 18 <= a <= 23:
#     print('Добрый вечер!')
# else:
#     print('error')
#
# #3.
# a = 21
# b = 4111
# c = 122
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)
#
# #4.
# a = int(input())
# b = int(input())
# c = input()
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     if not b:
#         print("You can't divide by zero!")
#     else:
#         print(a / b)
#
# #5.
# a = int(input())
# if a % 4 == 0 and a % 100 != 0:
#     print("yes")
# elif a % 400 == 0:
#     print("yes")
# else:
#     print('no')

# # task 1
# logs = [
#     "2026-02-19 10:00:01 INFO  Start suite",
#     "2026-02-19 10:00:02 ERROR Login failed",
#     "2026-02-19 10:00:03 ERROR Payment failed IGNORED",
#     "2026-02-19 10:00:04 WARN  Slow response",
#     "2026-02-19 10:00:05 ERROR DB timeout",
#     "2026-02-19 10:00:06 ERROR IGNORED flaky test",
# ]
# errors = []
# for el in logs:
#     if "ERROR" in el and "IGNORED" not in el:
#         errors.append(el)
# print(errors)
#
# # task 2
# responses = [
#     "GET /api/users status=200",
#     "GET /api/login status=401",
#     "GET /api/orders status=200",
#     "GET /api/pay status=500",
#     "GET /api/pay status=500 retry",
# ]
# idx = 0
# for el in range(len(responses)):
#     if 'status=500' in responses[el]:
#         idx = el
#         break
# print(idx)
#
# # task 3
# sequence = [False, False, True, True]  # дальше считаем, что остаётся True
#
# def check_ready(seq):
#     i = 0
#     def count():
#         nonlocal i
#         if i > len(seq):
#             return True
#         else:
#             status = seq[i]
#             i += 1
#         return status
#     return count
#
# check = check_ready(sequence)
# ready = False
# attempts = 0
# while not ready and attempts < 5:
#     ready = check()
#     attempts += 1
# print(ready)
# print(attempts)
#
# # task 4
# browsers = ["chrome", "firefox"]
# tests = ["login", "logout", "profile"]
#
# results = {
#     ("chrome", "login"): "passed",
#     ("chrome", "logout"): "failed",
#     ("chrome", "profile"): "passed",
#     ("firefox", "login"): "passed",
#     ("firefox", "logout"): "passed",
#     ("firefox", "profile"): "failed",
# }
#
# lines = []
# # keys = [] # отладка
# for b in browsers:
#     for t in tests:
#         pair = list(zip([b], [t]))
#         for i in pair:
#             for k, v in results.items():
#                 if i == k:
#                     # keys.append(i) # отладка
#                     lines.append(f'{b}:{t}={v}')
# print(lines)
#
# # task 5
# expected = ["ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"]
# actual   = ["ok", "fail", "ok", "fail", "ok", "fail", "fail", "ok"]
#
# mismatch_indexes = []
# while len(mismatch_indexes) < 4:
#     inx = 0
#     for i, j in zip(expected, actual):
#         if i != j:
#             mismatch_indexes.append(inx)
#         inx += 1
# print(mismatch_indexes)

# new 1
# events = [
#     "INFO boot ok",
#     "WARN cache miss",
#     "ERROR db timeout",
#     "WARN retry scheduled",
# ]
# i = -1
# for j, el in enumerate(events):
#     if 'CRITICAL' in el:
#         i = j
#         break
# print(i)

# new 2
# tokens = ["", "", "", "abc123", "xyz999"]  # пустая строка = токена нет
#
# def make_get_token(seq):
#     i = 0
#     def get_token():
#         nonlocal i
#         val = seq[i] if i < len(seq) else "last_token"
#         i += 1
#         return val
#     return get_token
#
# get_token = make_get_token(tokens)
# token = ''
# attempts = 0
# while (not token) and attempts < 4:
#     token = get_token()
#     attempts += 1
# if not token:
#     token = None
# print(token, attempts, sep='\n')

# new 3
# checks = ["down", "down", "up", "up"]
#
# def make_ping(seq):
#     i = 0
#     def ping():
#         nonlocal i
#         val = seq[i] if i < len(seq) else "up"
#         i += 1
#         return val
#     return ping
#
# ping = make_ping(checks)
# status = ''
# attempts = 0
# while (status != 'up') and (attempts < 5):
#     status = ping()
#     attempts += 1
# print(status)
# print(attempts)

# new 4
# roles = ["guest", "user", "admin"]
# actions = ["read", "write"]
#
# permissions = {
#     ("guest", "read"): True,
#     ("guest", "write"): False,
#     ("user", "read"): True,
#     ("user", "execute"): True,
#     ("admin", "read"): True,
#     ("admin", "write"): True,
# }
# lines = []
# for r in roles:
#     for a in actions:
#         status = permissions.get((r, a), False)
#         if status:
#             lines.append(f'{r} {a}: ALLOW')
#         else:
#             lines.append(f'{r} {a}: DENY')
# print(lines)

# # new 5
# steps = [
#     ("open_app", "ok"),
#     ("login", "fail"),
#     ("open_profile", "ok"),
#     ("upload_avatar", "fail"),
#     ("save", "fail"),
#     ("logout", "fail"),
# ]
# failed_steps = []
# failed = 0
# for el in steps:
#     if el[1] == 'fail':
#         failed_steps.append(el[0])
#         failed += 1
#     if failed == 3:
#         break
# print(failed_steps)

# boss
# attempt_logs = [
#     [
#         "INFO start test=login",
#         "WARN captcha required",
#         "ERROR step=auth msg=timeout",
#         "INFO end test=login",
#     ],
#     [
#         "INFO start test=login",
#         "ERROR step=auth msg=timeout IGNORED",
#         "ERROR step=ui msg=button_not_found",
#         "INFO end test=login",
#     ],
#     [
#         "INFO start test=login",
#         "INFO step=auth ok",
#         "INFO step=ui ok",
#         "INFO result=PASS",
#         "INFO end test=login",
#     ],
# ]
# # summary = {
# #     "attempts_used": 3,                 # сколько попыток реально использовали
# #     "final_status": "PASS",             # "PASS" если в логах попытки есть "result=PASS", иначе "FAIL"
# #     "errors_total": 2,                  # сколько ERROR всего, но НЕ считать строки с "IGNORED"
# #     "error_steps": ["auth", "ui"],      # уникальные step из ERROR (без IGNORED) в порядке первого появления
# # }
# summary = {
#     "attempts_used": 0,
#     "final_status": None,
#     "errors_total": 0,
#     "error_steps": None,
# }
# unique_steps = []
# passed = False
# for attempt in attempt_logs:
#     if not passed:
#         summary['final_status'] = 'FAIL'
#         for status in attempt:
#             if 'ERROR' in status and 'IGNORED' not in status:
#                 summary['errors_total'] += 1
#                 if 'step' in status:
#                     step = ''
#                     for i in range(status.find('=') + 1, len(status)):
#                         if status[i] != ' ':
#                             step += status[i]
#                         else:
#                             break
#                     if step not in unique_steps:
#                         unique_steps.append(step)
#             if 'result=PASS' in status:
#                 passed = True
#                 summary['final_status'] = 'PASS'
#                 break
#         summary['attempts_used'] += 1
#     else:
#         break
# summary['error_steps'] = unique_steps
# print(summary)

# extract str
# line = "ERROR step=auth msg=timeout IGNORED"
# step = line.split("step=", 1)[1].split(' ', 1)[0]
# print(step)
# line1 = "2026-02-20 10:00:01 ERROR   step=auth    msg=timeout   "
# step = line1.split('step=', 1)[1].split(' ', 1)[0]
# print(step)
# line2 = "WARN retrying... ERROR msg=button_not_found; step=ui; screenshot=on"
# step = line2.split('step=', 1)[1].split(';', 1)[0]
# print(step)

# clean 1
# nums = [10, 15, 50, 49, 51, 60]
# idx = -1
# for i, num in enumerate(nums):
#     if num > 50:
#         idx = i
#         break
# print(idx)

# # clean 2
# nums = [3, -1, 0, 5, -7, 2, 0, 10]
# total = 0
# for num in nums:
#     if num <= 0:
#         continue
#     total += num
# print(total)

# # clean 3
# s = "autotest"
# s_lst = list(s)
# left = 0
# right = len(s_lst) - 1
# while left < right:
#     s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
#     left += 1
#     right -= 1
# reversed_s = ''.join(s_lst)
# print(reversed_s)

# items = [1, 1.0, "1", True, None, [1, 2], (1, 2), {1, 2}, {"a": 1}]
# info = []
# mutable = ''
# for item in items:
#     mutable = 'mutable=no'
#     if type(item) in [list, dict, set]:
#         mutable = 'mutable=yes'
#     info.append(f'{type(item).__name__} {mutable}')
# print(info)

# a = [1, 2, 3]
# b = a
# c = a[:]   # копия списка через срез
# b.append(4)
# c.append(5)
# print(a, b, c)

# codes = [200, 201, 302, 404, 418, 500, 503, 123]
# labels = []
# for code in codes:
#     if 200 <= code <= 299:
#         labels.append('ok')
#     elif 300 <= code <= 399:
#         labels.append('redirect')
#     elif 400 <= code <= 499:
#         labels.append('client_error')
#     elif 500 <= code <= 599:
#         labels.append('server_error')
#     else:
#         labels.append('unknown')
# print(labels)

# values = [0, 1, "", "ok", [], [1], None, False, True]
# result = []
# for value in values:
#     if value is None:
#         result.append('none')
#     elif not value:
#         result.append('empty')
#     else:
#         result.append('value')
# print(result)
# a = [1]
# print(a[-2])

# 1/5 — ZIP
# names = ["login", "logout", "profile", "search"]
# durations = [1.2, 0.8, 2.5, 1.0]
# statuses = ["passed", "failed", "passed", "failed"]
#
# records = list(zip(names, durations, statuses))
# failed_names = []
# for record in records:
#     if record[-1] == 'failed':
#         failed_names.append(record[0])
# print(records)
# print(failed_names)

# 2/5 — LIST
# runs = ["passed", "passed", "failed", "failed", "failed", "passed", "passed", "failed"]
# compressed = []
# prev = ''
# for run in runs:
#     if run != prev:
#         compressed.append(run)
#     prev = run
# switches = len(compressed) - 1
# print(compressed)
# print(switches)

# 3/5 — TUPLE
# clicks = [(10, 5), (7, 12), (10, 5), (3, 4), (7, 12), (7, 12)]
# unique_clicks = []
# last_click = clicks[-1]
# for click in clicks:
#     if click in unique_clicks:
#         continue
#     unique_clicks.append(click)
# print(unique_clicks)
# print(last_click)
# # второе решение
# unique_clicks = list(set(clicks))
# print(unique_clicks)

# 4/5 — SET
# expected = {"login", "logout", "profile", "search"}
# actual = {"login", "profile", "search", "settings"}
# missing = expected - actual
# extra = actual - expected
# common = expected & actual
# print(missing)
# print(extra)
# print(common)

# 5/5 — DICT
# statuses = ["passed", "failed", "failed", "skipped", "passed", "failed", "passed"]
# count = {}
# most_common = []
# for status in statuses:
#     if status not in count:
#         count[status] = 0
#     count[status] += 1
# max_count = max(count.values())
# for k, v in count.items():
#     if v == max_count:
#         most_common.append(k)
#
# print(count)
# print(sorted(most_common))

# 1/5 — zip + обработка разной длины
# names = ["login", "logout", "profile", "search"]
# statuses = ["passed", "failed", "passed"]  # короче!
# pairs = []
# for i, n in enumerate(names):
#     if i < len(statuses):
#         pairs.append((n, statuses[i]))
#     else:
#         pairs.append((n, 'unknown'))
# print(pairs)

# dict (агрегация) + list (порядок)
# events = [
#     "login:passed",
#     "logout:failed",
#     "login:failed",
#     "search:passed",
#     "login:passed",
#     "search:failed",
# ]
# stats = {}
# order = []
# for e in events:
#     name = e.split(':')[0]
#     status = e.split(':')[1]
#     if name not in stats:
#         stats[name] = {'passed': 0, 'failed': 0}
#         order.append(name)
#     if status == 'passed':
#         stats[name]['passed'] += 1
#     else:
#         stats[name]['failed'] += 1
#
# print(stats)
# print(order)

# calls = [
#     ("/login", 200),
#     ("/users", 200),
#     ("/login", 401),
#     ("/pay", 500),
#     ("/users", 500),
#     ("/pay", 500),
# ]
# unique_endpoints = []
# failed_endpoints = set()
# failed_in_order = []
# for c in calls:
#     if c[0] not in unique_endpoints:
#         unique_endpoints.append(c[0])
#     if c[1] >= 500:
#         failed_endpoints.add(c[0])
# for el in unique_endpoints:
#     if el in failed_endpoints:
#         failed_in_order.append(el)
# print(unique_endpoints)
# print(failed_endpoints)
# print(failed_in_order)

# tuple + распаковка + list
# pairs = ["user=alice", "id=42", "active=True", "role=admin"]
# kv = []
# keys = []
# values = []
# for pair in pairs:
#     key, value = pair.split('=')
#     kv.append((key, value))
#     keys.append(key)
#     values.append(value)
# print(kv)
# print(keys)
# print(values)

# dict + сортировка + set
# names = ["login", "logout", "login", "search", "login", "search", "profile"]
# counts = {}
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# lst = sorted(counts, key=lambda n: (-counts[n], n))
# top2 = lst[:2]
# print(lst)
# print(counts)
# print(top2)

# Функции 1/5
# responses = [
#     "GET /health status=200",
#     "GET /login status=401",
#     "GET /users status=200",
#     "GET /pay status=500",
#     "GET /pay status=500 retry",
# ]
# def first_status_index(lines, status_code):
#     for i, line in enumerate(lines):
#         response = f'status={status_code}'
#         if response in line:
#             return i
#     return -1
# print(first_status_index(responses, 500))
# print(first_status_index(responses, 404))

# Функции 2/5
# def build_url(host, path, https=True):
#     if https:
#         return f'https://{host}/{path.lstrip("/")}'
#     return f'http://{host}/{path.lstrip("/")}'
# print(build_url("example.com", "api/users"))
# print(build_url("example.com", "/api/users", https=False))

# Функции 3/5
# def normalize_status(code):
#     if 200 <= code <= 299:
#         return 'ok'
#     elif 400 <= code <= 499:
#         return 'client_error'
#     elif 500<= code <= 599:
#         return 'server_error'
#     else:
#         return 'unknown'
# print(normalize_status(204))
# print(normalize_status(404))
# print(normalize_status(503))
# print(normalize_status(302))

# Функции 4/5
# tests = [
#     {"name": "login", "duration": 1.2},
#     {"name": "search", "duration": 2.5},
#     {"name": "logout", "duration": 0.8},
#     {"name": "profile", "duration": 2.5},
# ]
# def sorting_tests(tests):
#     sorted_tests = sorted(tests, key= lambda x:(-x['duration'], x['name']))
#     return sorted_tests
# print(sorting_tests(tests))

# Функции 5/5
# BASE_TIMEOUT = 10
# def get_timeout(timeout=None):
#     if timeout is None:
#         return BASE_TIMEOUT
#     return timeout
# print(get_timeout())
# print(get_timeout(3))
# print(get_timeout(0))

# Срезы 1/3
# logs = [
#     "INFO start",
#     "WARN slow",
#     "INFO step1 ok",
#     "ERROR timeout",
#     "INFO retry",
#     "INFO step1 ok",
#     "INFO end",
# ]
# n = 3
# print(logs[-n:])

# Срезы 2/3
# tests = ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8"]
# even = tests[::2]
# odd = tests[1::2]
# every3_from2 = tests[2::3]
# print(even)
# print(odd)
# print(every3_from2)

# Срезы 3/3
# s = "autotest"
# start = 3
# end = 50
# part = s[start:end]
# print(part)

# Практика 1/2
# lines = [
#     "# Report generated: 2026-02-22",
#     "# Suite: smoke",
#     "test_login: passed",
#     "test_logout: failed",
#     "test_profile: passed",
#     "# END",
# ]
# body = lines[2:-1]
# print(body)

# Практика 2/2
# logs = [
#     "INFO start",
#     "INFO step1 ok",
#     "WARN slow",
#     "INFO step2 ok",
#     "ERROR timeout",
#     "INFO retrying",
#     "INFO step2 ok",
#     "INFO end",
# ]
# error_index = 4
# window = 2
# start = error_index - window
# end = error_index + window + 1
# if start < 0:
#     start = 0
# if end > len(logs):
#     end = len(logs)
# context = logs[start:end]
# print(context)

# # 1/5 — парсинг строки “key=value; …” в числа
# line = "user=alice; status=200; time=1.234"
# # user, status, time =
# user = line.split('user=')[1].split(';')[0].strip()
# status = int(line.split('status=')[1].split(';')[0].strip())
# time = float(line.split('time=')[1].split(';')[0].strip())
# print(user)
# print(status)
# print(time)

# # 2/5 — нормализация пробелов в строке
# text = "  Login   OK \n  Status:\t200   "
# lst = text.split()
# normalized = ' '.join(lst)
# print(normalized)

# # 3/5 — безопасное преобразование в int (учесть знак)
# values = ["10", "-7", "  42 ", "+5", "3.14", "abc", "", "  -0  "]
# parsed = []
# # for value in values:
# #     try:
# #         parsed.append(int(value))
# #     except ValueError:
# #         parsed.append(None)
# for value in values:
#     stripped_value = value.strip()
#     if not stripped_value:
#         parsed.append(None)
#     elif stripped_value[0] in ['+', '-']:
#         if stripped_value[1:].isdigit():
#             parsed.append(int(stripped_value))
#         else:
#             parsed.append(None)
#     elif stripped_value.isdigit():
#         parsed.append(int(stripped_value))
#     else:
#         parsed.append(None)
# print(parsed)

# 4/5 — f-string форматирование.
# test_name = "login"
# duration = 1.203456
# attempts = 3
# msg = f'Test {test_name} took {duration:.2f}s (attempts={attempts})'
# print(msg)

# # 5/5 — f-string + проценты + защита от деления на ноль
# failed = 3
# total = 17
# if total != 0:
#     report = f'Failed: {failed}/{total} ({(failed / total * 100):.2f}%)'
# else:
#     report = f'Failed: {failed}/{total} (N/A)'
# print(report)

# Исключения 1/5 — безопасный int
# values = ["10", "x", None, " 5 ", "3.14", "-7"]
# def safe_int(x):
#     try:
#         return int(x)
#     except ValueError:
#         return None
#     except TypeError:
#         return None
# print([safe_int(v) for v in values])

# # Исключения 2/5 — raise с понятным сообщением
# config_ok = {"host": "example.com", "token": "abc123"}
# config_bad = {"host": "example.com"}
# def require_token(config):
#     if 'token' not in config or config['token'] == '':
#         raise ValueError('token is required')
#     return config['token']
# print(require_token(config_ok))
# print(require_token(config_bad))

# Исключения 3/5 — try/except/else
# pairs = [("10", "2"), ("5", "0"), ("x", "3")]
# def safe_divide(a, b):
#     try:
#         c = int(a) / int(b)
#     except ValueError:
#         return None
#     except ZeroDivisionError:
#         return 'inf'
#     else:
#         return c
# print([safe_divide(a, b) for a, b in pairs])

# Исключения 4/5 — finally (гарантированное “закрытие”)
# actions = ["open", "work", "crash", "close"]
# def run_actions(actions):
#     opened = False
#     try:
#         for a in actions:
#             if a == 'open':
#                 opened = True
#             elif a == 'crash':
#                 raise RuntimeError('boom')
#     except RuntimeError:
#         opened = False
#     finally:
#         opened = False
#     return opened
#
#
# print(run_actions(["open", "work", "crash", "close"]))

# # Исключения 5/5 — собственное исключение + переподнятие с контекстом
# data = ["1", "2", "x", "3"]
# def sum_ints(values):
#     result = []
#     for i, v in enumerate(values):
#         try:
#             result.append(int(v))
#         except ValueError as e:
#             raise ValueError(f'bad value at index {i}: {v}') from e
#     return sum(result)
#
# print(sum_ints(["1","2","3"]))
# print(sum_ints(data))

# Мини-практика — парсер отчёта прогонов
# lines = [
#     "test=login status=passed duration=1.23",
#     "test=search status=failed duration=2.50",
#     "test=logout status=passed duration=0.80",
#     "test=profile status=failed duration=abc",      # битая duration
#     "test=pay status=passed duration=1.00",
#     "test=ui status=unknown duration=3.00",         # неизвестный статус
# ]
# def build_report(lines):
#     report = {
#     "total": 0,
#     "passed": 0,
#     "failed": 0,
#     "unknown": 0,
#     "avg_duration_passed": 0.0,
#     "bad_lines": [],
# }
#     passed_durations = []
#     for i, l in enumerate(lines):
#         report['total'] += 1
#         status = l.split('status=', 1)[1].split()[0].strip()
#         duration = l.split('duration=', 1)[1].split()[0].strip()
#         if status == 'passed':
#             report['passed'] += 1
#         elif status == 'failed':
#             report['failed'] += 1
#         else:
#             report['unknown'] += 1
#         try:
#             floated_duration = float(duration)
#             if status == 'passed':
#                 passed_durations.append(floated_duration)
#         except ValueError:
#             report['bad_lines'].append(i)
#     try:
#         avg_duration = sum(passed_durations) / len(passed_durations)
#     except ZeroDivisionError:
#         avg_duration = 0.0
#     report['avg_duration_passed'] = float(f'{avg_duration:.2f}')
#     return report
# print(build_report(lines))

# # 1/5 — Файлы: прочитать и посчитать
# def count_errors(path):
#     with open(path, 'r') as p:
#         content = p.read()
#         count = 0
#         for e in content.splitlines():
#             if 'ERROR' in e:
#                 count += 1
#     return count
# with open('log.txt', 'w') as l:
#     l.write('INFO start\n')
#     l.write('ERROR timeout\n')
#     l.write('WARN slow\n')
#     l.write('ERROR db\n')
#     l.write('INFO end\n')
# print(count_errors('log.txt'))

# # 2/5 — записать report.txt
# results = ["login:passed", "logout:failed", "search:passed", "profile:failed"]
# def write_report(path, results):
#     with open(path, 'w') as p:
#         f = 0
#         for r in results:
#             name, status = r.split(':')
#             if status == 'failed':
#                 f += 1
#             p.write(f'{name} -> {status}\n')
#         p.write(f'Total: {len(results)}, Failed: {f}')
#     return path
# with open(write_report('report.txt', results)) as r:
#     content = r.read()
# print(content)

# # 3/5 — import и структура проекта (без запуска)
# from utils.formatting import format_status

# # 4/5 — счётчик вызовов
# def make_counter(start=0):
#     count = start
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# c = make_counter(10)
# print(c())
# print(c())
#
# d = make_counter()
# print(d())
# print(d())

# 5/5 — фильтр логов по уровню
# logs = [
#     "INFO start",
#     "WARN slow",
#     "ERROR timeout",
#     "INFO retry",
#     "ERROR db",
# ]
# def make_level_filter(level):
#     def filter_logs(lines):
#         res = []
#         for l in lines:
#             if level in l:
#                 res.append(l)
#         return res
#     return filter_logs
# error_filter = make_level_filter("ERROR")
# print(error_filter(logs))
#
# info_filter = make_level_filter("INFO")
# print(info_filter(logs))
# def count_words(text: str) -> int:
#     return len(text.split())
# print(count_words(" Hello my                  friend "))

# def is_unique_char(s: str):
    # for i, ch in enumerate(s):
    #     if ch not in s[:i] and ch not in s[i + 1:]:
    #         return ch
    # return None
    #     count = {}
    #     for ch in s:
    #         count[ch] = count.get(ch, 0) + 1
    #     for k, v in count.items():
    #         if v == 1:
    #             return k
    #     return None
    # print(is_unique_char('aaaaaaastttttszdv'))

# def example(x=None):
#     if x is None:
#         x = []
#     x.append(1)
#     return x
# print(example())
# print(example())
# print(example())

