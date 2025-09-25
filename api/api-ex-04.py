#!/usr/bin/env python3
# Zadanie 4: Fizyczne właściwości
# Pobierz dane o Pikachu i wyświetl jego wzrost (height) oraz wagę (weight).

import requests
import json # json nie potrzebny w tym przypadku

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()

# mimo skróconej wersji powinna być obsługa warunku
if response.status_code == 200:
    print(f"Name: {(data["name"]).title()}")
    print(f"Height: {data["height"]}")
    print(f"Weight: {data["weight"]}")

# ----------- Future Tips: -----------
