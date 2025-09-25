#!/usr/bin/env python3
# Zadanie 5: Pierwsza funkcja
# Napisz funkcję `get_pokemon_name(pokemon_id)`, która zwraca nazwę pokemona na podstawie jego ID.

import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"
def get_pokemon_name(pokemon_id):
    response = requests.get(f"{baseUrl}{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        name = (data["name"]).title()
        return name

print(get_pokemon_name(12))

# ----------- Future Tips: -----------
