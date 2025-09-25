#!/usr/bin/env python3
# Zadanie 2: Wykonaj operacje na słowniku
# Wykonaj następujące operacje:
# - Usuń parę klucz-wartość 'profession'
# - Wyświetl wszystkie pary klucz-wartość w słowniku
# - Sprawdź czy klucz 'age' istnieje w słowniku

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
del my_dict["profession"]
print(my_dict)
if my_dict["age"]:
    print("Age key exists!")
else:
    print("Age key does not exist!")

# ----------- Future Tips: -----------
# do wyświetlenia obiektów można użyć
# metody items():
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
# istnienie klucza można sprawdzić również
# krótko za pomocą:
# print("Czy 'age' istnieje?", 'age' in my_dict)
