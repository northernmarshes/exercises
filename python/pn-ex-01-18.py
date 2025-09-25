#!/usr/bin/env python3
# Exercise 18: Check if a given year is a leap year
# A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.
# Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
# Write a code find if a given year is a leap year.

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
