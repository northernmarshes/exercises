#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 9: Zmodyfikuj zagnieżdżony słownik
# W poniższym słowniku zmień name na 'Jessa'.

nested_student_dict = {
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

nested_student_dict["class"]["student"].update({"name":"Jessa"})
print(nested_student_dict)

# ----------- Future Tips: -----------
# easy
