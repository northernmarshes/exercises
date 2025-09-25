#!/usr/bin/env python3
# Zadanie 4: Stwórz funkcję z argumentem domyślnym
# Napisz program tworzący funkcję show_employee() o następujących specyfikacjach:
# - Powinna przyjmować imię i pensję pracownika
# - Powinna wyświetlać imię i pensję
# - Jeśli pensja nie jest podana, powinna domyślnie wynosić 9000

def show_employee(name, salary="9000"):
        print(f"Name: {name}")
        print(f"Salary: {salary}")

show_employee("John", 3500)
show_employee("John")

# ----------- Future Tips: -----------
