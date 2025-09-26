#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 7: Sprawdzanie istnienia
# Napisz funkcję `pokemon_exists(name_or_id)`, która zwraca True/False w zależności od tego, czy pokemon istnieje.

import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"
def pokemon_exists(param):
    response = requests.get(f"{baseUrl}{param}")
    if response.status_code == 200:
        return True
    else:
        return False

print(pokemon_exists(12))
print(pokemon_exists("kotek"))

# ----------- Future Tips: -----------
