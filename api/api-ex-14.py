#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 14: Pierwsze ruchy
# Pobierz dane o Pikachu i wyświetl nazwy pierwszych 5 ruchów, które zna.
import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"

def first_5_moves(name_or_id):
    """wyświetla pierwsze 5 ataków"""
    try:
        response = requests.get(f"{baseUrl}{name_or_id}")
        response.raise_for_status()
        data = response.json()
        moves = []
        for move in data["moves"][:5]:
            moves.append(move["move"]["name"])
        return moves
    except requests.exceptions.RequestException:
        return None
print(first_5_moves("pikachu"))

# ----------- Future Tips: -----------
# limitujemy iteracje zawężając listę
