#!/usr/bin/env python3
# Zadanie 2: Dodaj nowy string w środku danego stringa
# Mając dwa stringi s1 i s2, napisz program do stworzenia nowego stringa s3 przez dodanie s2 w środku s1.

def popinthemiddle(word, insert):
    middle_index = (len(word)//2)
    left = word[0:middle_index]
    right = word[middle_index:(len(word))]
    return (left + insert + right)

s1 = "Ault"
s2 = "Kelly"

print(popinthemiddle(s1 ,s2))

# ----------- Future Tips: -----------
# round(len(word)/2)
# może czasem dać wynik nieoczekiwany,
# bo round() zaokrągla do najbliższej liczby
# całkowitej (dla .5 do parzystej)!!
#
# Nie trzeba podawać końca - jeszcze lepiej:
# middle_index = len(s1) // 2
# return s1[:middle_index] + s2 + s1[middle_index:]
