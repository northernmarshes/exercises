#!/usr/bin/env python3
# Zadanie 13: Liczenie ruchów
# Napisz funkcję, która zwraca liczbę ruchów (moves), które zna dany pokemon.
import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"

def get_move_count(name_or_id):
    """wyświetla liczbę ataków"""
    try:
        response = requests.get(f"{baseUrl}{name_or_id}")
        response.raise_for_status()
        data = response.json()
        move_count = len(data["moves"])
        return move_count
    except requests.exceptions.RequestException:
        return None
print(get_move_count("metapod"))

# ----------- Future Tips: -----------
# all fine
