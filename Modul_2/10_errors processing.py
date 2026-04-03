#1.
# def safe_divide(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Can't divide on zero"
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
# print(safe_divide(2, 0))

#2.
# try:
#     a = int(input("Enter a number"))
#     print(f"You've entered a {a}")
# except ValueError:
#     print("Error: you have to input a number")

#3.
# try:
#     a = 1 + "a"
#     print("On working")
# except TypeError:
#     print("U gay")
# finally:
#     print("Ending")

#4.
# def check_age(age):
#     if age > 18:
#         print("Access approved")
#     else:
#         raise ValueError("You have to be 18 or older")
# check_age(20)
# check_age(17)

#5.
try:
    a = int(input("Enter a number: "))
    print(100/a)
except ValueError:
    print("You have to input a number")
except ZeroDivisionError:
    print("Can't divide on zero")
finally:
    print("End of the program")
