#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 12: Obrazki pokemona
# Wyświetl URL obrazka (sprite) Pikachu - zarówno przednią, jak i tylną wersję.

import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"

def get_pics_urls(name_or_id):
    try:
        response = requests.get(f"{baseUrl}{name_or_id}")
        response.raise_for_status()
        data = response.json()
        front = data["sprites"]["front_default"]
        back = data["sprites"]["back_default"]
        return front, back
    except requests.exceptions.RequestException:
        return none
print(get_pics_urls("pikachu"))

# ----------- Future Tips: -----------
