#!/usr/bin/env python3
# Zadanie 6: Stwórz funkcję rekurencyjną
# Napisz program tworzący funkcję rekurencyjną obliczającą sumę liczb od 0 do 10.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# ----------- Future Tips: -----------
# Też działa ale nie o to chodzi:
# result = 0
# for val in range(0,11):
#     result = result + val
# print (result)
#
# Recursion: dodawanie od końca aż nie dojdzie do 0 albo 1
#
# Jeszcze prościej:
# def suma_rekurencyjna(n):
#     if n == 0:
#         return 0
#     else:
#         return n + suma_rekurencyjna(n - 1)
# print(suma_rekurencyjna(10))
