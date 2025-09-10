#!/usr/bin/env python3
import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"
def get_pokemon_basic_info(name_or_id):
    try:
        response = requests.get(f"{baseUrl}{name_or_id}")
        response.raise_for_status()
        data = response.json()
        return {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
        }
    except requests.exceptions.RequestException:
        return None

print(get_pokemon_basic_info("charmander"))
print(get_pokemon_basic_info("mankey"))
print(get_pokemon_basic_info("raichu"))
print(get_pokemon_basic_info("jigglypuff"))
