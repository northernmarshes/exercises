#!/usr/bin/env python3
# Zadanie 10: Funkcja do typów
# Napisz funkcję, która zwraca listę typów dla dowolnego pokemona.

import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"

def get_all_types(name_or_id):
    try:
        response = requests.get(f"{baseUrl}{name_or_id}")
        response.raise_for_status()
        data = response.json()
        types = [type_info["type"]["name"] for type_info in data["types"]]
        return types
    except requests.exceptions.RequestException:
        return None
print(get_all_types("zapdos"))
