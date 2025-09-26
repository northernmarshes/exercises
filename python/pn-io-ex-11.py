#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 11: Percentage Display
# Ask the user for a numerator and a denominator. Calculate the percentage and display it with two decimal places followed by a percent sign (e.g., 75.50%).

def percent ():
    numerator = int(input("Give me a numerator "))
    denominator = int(input("And a denominator "))

    percentage = (numerator * 100) / denominator

    print (f"The percentage is {percentage:.2f}%")

percent()

# ----------- Future Tips: -----------
# Dodajemy obsługę błędów i dzielenia przez zero:
# try:
#     numerator = float(input("Enter the numerator: "))
#     denominator = float(input("Enter the denominator: "))
#     if denominator == 0:
#         print("Error: Denominator cannot be zero.")
#     else:
#         percentage = (numerator / denominator) * 100
#         print(f"The percentage is: {percentage:.2f}%")
# except ValueError:
#     print("Invalid input. Please enter numbers.")
