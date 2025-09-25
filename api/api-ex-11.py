#!/usr/bin/env python3
# Zadanie 11: Umiejętności pokemona
# Pobierz dane o Pikachu i wyświetl nazwy wszystkich jego umiejętności (abilities).

import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"

def get_abilities(name_or_id):
    try:
        response = requests.get(f"{baseUrl}{name_or_id}")
        response.raise_for_status()
        data = response.json()
        abilities = [ability["ability"]["name"] for ability in data["abilities"]]
        return abilities
    except requests.exceptions.RequestException:
        return None
print(get_abilities("pikachu"))

# ----------- Future Tips: -----------
