#!/usr/bin/env python3

def percent ():
    numerator = int(input("Give me a numerator "))
    denominator = int(input("And a denominator "))

    percentage = (numerator * 100) / denominator

    print (f"The percentage is {percentage:.2f}%")

percent()

# dodajemy obsługę błędów i dzielenia przez zer# o
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
