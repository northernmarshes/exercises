#!/usr/bin/env python3
# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

number1 = 40
number2 = 30
product = (number1 * number2)

if product < 1000:
    print (product)
else:
    print (number1 + number2)

# ----------- Future Tips: -----------
# Moje rozwiązenie było poprawne ale nie zawierało
# operatora <= oraz nie było opisane w formie funkcji
#
# Rozwiązanie:
# def multiplication_or_sum(num1, num2):
#     product = num1 * num2
#     if product <= 1000:
#         return product
#     else:
#         return num1 + num2
#
# result = multiplication_or_sum(20, 30)
# print("The result is", result)
# result = multiplication_or_sum(40, 30)
# print("The result is", result)
