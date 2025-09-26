#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 6: Obsługa błędów
# Rozszerz poprzednią funkcję o obsługę błędów - sprawdź status odpowiedzi przed próbą pobrania danych JSON.

import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"
def get_pokemon_name(pokemon_id):
    response = requests.get(f"{baseUrl}{pokemon_id}")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        name = (data["name"]).title()
        return name
print (get_pokemon_name(12))

# ----------- Future Tips: -----------
