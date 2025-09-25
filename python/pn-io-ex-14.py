#!/usr/bin/env python3
# Exercise 14: Tabular Output from Lists
# You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these lists as a simple table with columns “Name” and “Score”.

from prettytable import PrettyTable

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

t = PrettyTable()
rows = []

t.add_column('Name', names)
t.add_column('Score', scores)

print(t)

# ----------- Future Tips: -----------
# Formatowanie bez zewnętrznych bibliotek:
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
# print(f"{'Name':<10} {'Score':<5}")
# print("-" * 15)
# for name, score in zip(names, scores):
#     print(f"{name:<10} {score:<5}")
