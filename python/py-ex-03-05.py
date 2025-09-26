#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 5: Stwórz funkcję wewnętrzną
# Stwórz program z zagnieżdżonymi funkcjami do wykonania dodawania:
# - Zdefiniuj funkcję zewnętrzną przyjmującą parametry a i b
# - Wewnątrz zdefiniuj funkcję wewnętrzną obliczającą sumę a i b
# - Funkcja zewnętrzna powinna dodać 5 do tej sumy i zwrócić wynik

def addition01(a,b):
    def addition02(a,b):
        wynik1 = a + b
        return wynik
    wynik2 = addition02(a,b) + 5
    print (wynik2)
addition01(5,4)

# ----------- Future Tips: -----------
# parametry w wewnętrznej funkcji nie są potrzebne:
# def addition01(a,b):
#     def addition02():
#         wynik1 = a + b
#         return wynik
#     wynik2 = addition02() + 5
#     print (wynik2)
# addition01(5,4)
