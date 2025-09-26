#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 2: Sprawdzanie typu JSON
# Sprawdź, czy odpowiedź z poprzedniego zadania zawiera dane JSON. Wyświetl typ obiektu zwróconego przez `.json()`.

import requests
import json

baseUrl = "https://pokeapi.co/api/v2/"
url = (f"{baseUrl}pokemon/pikachu")

def status():
    response = requests.get(url)
    return response

response = status()
print (f"Typ danych to: {type(response.json())}")

# ----------- Future Tips: -----------
