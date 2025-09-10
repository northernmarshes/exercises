#!/usr/bin/env python3

number1 = 40
number2 = 30
product = (number1 * number2)

if product < 1000:
    print (product)
else:
    print (number1 + number2)

# moje rozwiązenie było poprawne ale nie zawierało operatora <= oraz nie było opisane w formie funkcji

# rozwiązanie:
# def multiplication_or_sum(num1, num2):
#     product = num1 * num2
#     if product <= 1000:
#         return product
#     else:
#         return num1 + num2

# result = multiplication_or_sum(20, 30)
# print("The result is", result)

# result = multiplication_or_sum(40, 30)
# print("The result is", result)
