#!/usr/bin/env python3
# Zadanie 8: Wyświetl wartość klucza 'history' z zagnieżdżonego słownika
# Wyświetl wartość klucza 'history' z poniższego zagnieżdżonego słownika.

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

history_mark = sampleDict["class"]["student"]["marks"]["history"]
print(f"Mike's history mark is {history_mark}")

# ----------- Future Tips: -----------
# もちろん
