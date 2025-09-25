#!/usr/bin/env python3
# Zadanie 4: Formatuj datę i czas
# Napisz kod, który wyświetli datę w następującym formacie:
# Nazwa_dnia Numer_dnia Nazwa_miesiąca Rok
from datetime import datetime, date

given_date = datetime(2020, 2, 25)
formated_date = given_date.strftime("%A %d %B %Y")
print(formated_date)

# ----------- Future Tips: -----------
# formatowanie po polsku
# import locale
# try:
#     locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')
#     formatted_date_pl = given_date.strftime("%A %d %B %Y")
#     print(f"Po polsku: {formatted_date_pl}")
# except:
#     print("Lokalizacja polska nie jest dostępna")
