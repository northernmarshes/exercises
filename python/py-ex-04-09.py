#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 9: Oblicz sumę i średnią cyfr w stringu
# Mając string s1, napisz program zwracający sumę i średnią cyfr występujących w stringu, ignorując wszystkie inne znaki.

str1 = "PYnative29@#8496"


def add_numbers(text):
    numbers = []
    suma = 0
    for char in text:
        if char.isdigit():
            numbers.append(int(char))
    suma = sum(numbers)
    srednia = suma / len(numbers)
    print(f"Suma liczb to {suma}")
    print(f"Średnia liczb to {srednia}")


add_numbers(str1)


#  ----------- Future Tips: -----------
