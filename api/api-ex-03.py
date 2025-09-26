#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 3: Podstawowe dane pokemona
# Pobierz dane o Pikachu i wyświetl tylko jego nazwę i ID.

import requests
import json

baseUrl = "https://pokeapi.co/api/v2/pokemon/"

def get_pokedata(pokename):
    url = (f"{baseUrl}{pokename}")
    response = (requests.get(url))
    status = response.status_code
    if status == 200:
        pokedata = response.json()
        return pokedata

name = "pikachu"
monsters = get_pokedata(name)
print ((monsters["name"]).title())
print (monsters["id"])

# ----------- Future Tips: -----------
