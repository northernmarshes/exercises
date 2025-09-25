#!/usr/bin/env python3
# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

list1= [10, 20, 25, 30, 35]
list2= [40, 45, 60, 75, 90]
result_list = []

def is_even(num1, num2):
   for val in num1:
       if (val % 2) != 0:
           result_list.append(val)
   for val in num2:
       if (val % 2) == 0:
           result_list.append(val)
   print (result_list)

is_even(list1, list2)

# ----------- Future Tips: -----------
# Do poprawy:
# Globalna zmienna result_list
# - to może prowadzić do problemów
# Brak return - funkcja tylko printuje,
# nie zwraca wyniku.
# Nazwa funkcji is_even - myląca, bo
# funkcja nie sprawdza czy coś jest parzyste
#
# Poprawiona wersja:
# def merge_odd_even(list1, list2):
#      result_list = []  # LOKALNA zmienna
#      for val in list1:
#          if (val % 2) != 0:  # nieparzyste z list1
#              result_list.append(val)
#      for val in list2:
#          if (val % 2) == 0:  # parzyste z list2
#              result_list.append(val)
#      return result_list  # ZWRACA wynik
# # Użycie:
# result = merge_odd_even(list1, list2)
# print("Result:", result)
