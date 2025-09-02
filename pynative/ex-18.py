#!/usr/bin/env python3
def isleap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f"The year {year} is a leap year.")
    elif year % 400 == 0:
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is NOT a leap year.")
isleap(2020)
isleap(2025)
