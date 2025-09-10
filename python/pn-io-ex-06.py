#!/usr/bin/env python3

"""moje rozwiązanie"""
file = open(r"/home/edna/Pulpit/CODE/python/pynative/input-output/test.txt", 'r')
tekst = str(file.read())
lines = tekst.split()
lines.remove('line5')
nowytekst = "\n".join(lines)
file = open("newfile.txt", 'x')
file.write(nowytekst)
file.close

"""pracując z plikami używamy with statement
oto poprawiona wersja tego programu"""

# with open("test.txt", 'r') as file:
#     lines = file.readlines()  # Zachowuje znaki nowej linii

# # Usuń 5. linię (indeks 4)
# if len(lines) > 4:
#     lines.pop(4)

# with open("new_file.txt", 'w') as file:
#     file.writelines(lines)
