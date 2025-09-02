#!/usr/bin/env python3
import requests

baseUrl = "https://pokeapi.co/api/v2/"
url = (f"{baseUrl}pokemon/pikachu")
response = requests.get(url)
print(f"Status: {response.status_code}")
