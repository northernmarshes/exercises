#!/usr/bin/env python3
# Zadanie 9: Typy pokemona
# Pobierz dane o Pikachu i wyświetl nazwy wszystkich jego typów (np. "electric").

import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"

def get_type(name_or_id):
    try:
        response = requests.get(f"{baseUrl}{name_or_id}")
        response.raise_for_status()
        data = response.json()
        return data["types"][0].get("type", {}).get("name")
    except requests.exceptions.RequestException:
        return None

print(get_type("onix"))

# ----------- Future Tips: -----------
# list comprehenshion - skrócony for loop do wyciągnięcia wszyskich elementów
# types = [type_info['type']['name'] for type_info in data['types']]
