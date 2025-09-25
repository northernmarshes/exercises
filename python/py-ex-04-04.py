#!/usr/bin/env python3
# Zadanie 4: Uporządkuj znaki tak aby małe litery były pierwsze
# Dany string zawiera kombinację małych i dużych liter. Napisz program do uporządkowania znaków tak aby wszystkie małe litery były pierwsze.

str1 = "PyNaTive"

def lowerfirst(word):
    lower = ""
    upper = ""
    for char in word:
        if char.islower() == True:
            lower = lower + char
        elif char.isupper() == True:
            upper = upper + char
    newword = lower + upper
    print (newword)

lowerfirst(str1)

# ----------- Future Tips: -----------
# Możnaby zrezygnować z == True
# oraz zwracać wynik zamiast drukować
