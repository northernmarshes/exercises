#!/usr/bin/env python3
import requests
import json

baseUrl = "https://pokeapi.co/api/v2/"
url = (f"{baseUrl}pokemon/pikachu")

def status():
    response = requests.get(url)
    return response

response = status()
print (f"Typ danych to: {type(response.json())}")
