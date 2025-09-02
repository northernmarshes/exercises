#!/usr/bin/env python3

# też działa ale nie o to chodzi
# result = 0
# for val in range(0,11):
#     result = result + val
# print (result)

#recursion - dodawanie od końca aż nie dojdzie do 0 albo 1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# jeszcze prościej:
# def suma_rekurencyjna(n):
#     if n == 0:
#         return 0
#     else:
#         return n + suma_rekurencyjna(n - 1)
# print(suma_rekurencyjna(10))
