#!/usr/bin/env python3
# Zadanie 3: Stwórz nowy string z pierwszych, środkowych i ostatnich znaków każdego stringa
# Mając dwa stringi s1 i s2, napisz program zwracający nowy string składający się z pierwszych, środkowych i ostatnich znaków s1 i s2.

def mixstrings(base, insert):
    middle_index01 = len(base)//2
    middle_index02 = len(insert)//2
    return base[0]+insert[0]+base[middle_index01]+insert[middle_index02]+base[-1]+insert[-1]

s1 = "America"
s2 = "Japan"

print(mixstrings(s1, s2))

# ----------- Future Tips: -----------
# Elegancko byłoby podzielić na:
# # Pierwsze znaki
# first_chars = s1[0] + s2[0]
# # Środkowe znaki
# middle_chars = s1[len(s1)//2] + s2[len(s2)//2]
# # Ostatnie znaki
# last_chars = s1[-1] + s2[-1]
# return first_chars + middle_chars + last_chars
