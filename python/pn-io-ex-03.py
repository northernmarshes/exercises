#!/usr/bin/env python3
# def dec_to_oct (s):
#     o = "%o" % int(s)
#     print (f"The octal representation of the decimal number {s} is {o}.")

# num = 8
# dec_to_oct(num)

# num = 8
# print (oct(int(num))[2:])

num = 8
print (f"The octal representation of the decimal number {num} is {num:o}.")



"""Wszystkie dostępne specyfikatory:"""
# %d - dziesiętny (decimal)
# %o - ósemkowy (octal)
# %x - szesnastkowy małymi literami
# %X - szesnastkowy wielkimi literami
# Niestety %b dla binarnego nie istnieje w tym systemie formatowania.

"""Nowocześniejszy sposób to:"""
# bin(8)  # '0b1000'
# oct(8)  # '0o10'
# hex(8)  # '0x8'
# # Z binarnego na dziesiętny:
# int('1010', 2)      # 10

"""Najnowszy to wykorzystanie fstringów"""
# num = 42

# f"{num:b}"    # '101010'  - binarny
# f"{num:o}"    # '52'      - ósemkowy
# f"{num:x}"    # '2a'      - hex małymi literami
# f"{num:X}"    # '2A'      - hex wielkimi literami
# f"{num:d}"    # '42'      - dziesiętny (domyślny)
