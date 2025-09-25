#!/usr/bin/env python3
# Zadanie 2: Wykonaj manipulacje na liście
# Wykonaj następujące operacje:
# - Zmień drugi element na 200
# - Dodaj 600 na koniec listy
# - Wstaw 300 na trzecią pozycję (indeks 2)
# - Usuń 600 z listy (po wartości)
# - Usuń element z indeksu 0

my_list = [10, 20, 30, 40, 50]
my_list[1] = 200
print(f"Dodano 200: {my_list}")
my_list.append(600)
print(f"Dodano 600: {my_list}")
my_list.insert(2, 300)
print(f"Dodano 300: {my_list}")
my_list.remove(600)
print(f"Usunięto 600: {my_list}")
del my_list[0]
print(f"Usunięto pierwszy element: {my_list}")

# ----------- Future Tips: -----------
# zadanie poprawnie wykonane :)
