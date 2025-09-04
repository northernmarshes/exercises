#!/usr/bin/env python3

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
