#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 18: Check if a given year is a leap year

def isleap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f"The year {year} is a leap year.")
    elif year % 400 == 0:
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is NOT a leap year.")
isleap(2020)
isleap(2025)

# ----------- Future Tips: -----------
