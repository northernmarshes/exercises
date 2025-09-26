#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 1: Import i podstawowe zapytanie
# Zaimportuj bibliotekę `requests` i wykonaj proste zapytanie GET do `https://pokeapi.co/api/v2/pokemon/pikachu`. Wyświetl tylko status odpowiedzi.

import requests

baseUrl = "https://pokeapi.co/api/v2/"
url = (f"{baseUrl}pokemon/pikachu")
response = requests.get(url)
print(f"Status: {response.status_code}")

# ----------- Future Tips: -----------
