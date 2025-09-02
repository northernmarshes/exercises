#!/usr/bin/env python3
from prettytable import PrettyTable

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

t = PrettyTable()
rows = []

t.add_column('Name', names)
t.add_column('Score', scores)

print(t)

# formatowanie bez zewnętrznych bibliotek
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# print(f"{'Name':<10} {'Score':<5}")
# print("-" * 15)
# for name, score in zip(names, scores):
#     print(f"{name:<10} {score:<5}")
