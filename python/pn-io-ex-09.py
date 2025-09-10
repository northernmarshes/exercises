#!/usr/bin/env python3

with open("test.txt", "r") as file:
    lines = file.read()

if lines == "":
    print("The file is empty!")
else:
    print("There is content in the file!")

# # moje rozwiązanie jest poprawne aczkolwiek
# # można też zmierzyć rozmiar pliku
# import os
# size = os.stat("test.txt").st_size
# if size == 0:
#     print('file is empty')
