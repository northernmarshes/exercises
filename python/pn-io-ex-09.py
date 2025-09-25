#!/usr/bin/env python3
# Exercise 9: Check File is Empty or Not
# Write a program to check if the given file is empty or not

with open("test.txt", "r") as file:
    lines = file.read()

if lines == "":
    print("The file is empty!")
else:
    print("There is content in the file!")

# ----------- Future Tips: -----------
# Moje rozwiązanie jest poprawne aczkolwiek
# można też zmierzyć rozmiar pliku tak:
# import os
# size = os.stat("test.txt").st_size
# if size == 0:
#     print('file is empty')
