#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 6: Write all content of a file into a new file by skipping line number 5

file = open(r"/home/edna/Pulpit/CODE/python/pynative/input-output/test.txt", 'r')
tekst = str(file.read())
lines = tekst.split()
lines.remove('line5')
nowytekst = "\n".join(lines)
file = open("newfile.txt", 'x')
file.write(nowytekst)
file.close

# ----------- Future Tips: -----------
# Pracując z plikami używamy with statement
# Poprawiona wersja tego programu
#
# with open("test.txt", 'r') as file:
#     lines = file.readlines()  # Zachowuje znaki nowej linii
#
# # Usuń 5. linię (indeks 4)
# if len(lines) > 4:
#     lines.pop(4)
#
# with open("new_file.txt", 'w') as file:
#     file.writelines(lines)
