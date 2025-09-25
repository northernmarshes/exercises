#!/usr/bin/env python3
# Zadanie 7: Przypisz inną nazwę funkcji i wywołaj przez nową nazwę
# Dana: def display_student(name, age): print(name, age)
# Przypisz nową nazwę show_student() i wywołaj przez nią.

def display_student(name, age):
    print(name, age)
nowa_nazwa = display_student
nowa_nazwa("John", 20)

# ----------- Future Tips: -----------
