#!/usr/bin/env python3
# Exercise 8: Format variables using string.format() method
# Write a program to use the string.format() method to format the following three variables according to the expected output.

totalMoney = 1000
quantity = 3
price = 450

print(f"I have {totalMoney:.0f} dollars so I can buy {quantity:.0f} football for {price:.2f} dollars.")

# ----------- Future Tips: -----------
# Chodziło o użycie metody format a więc:
# quantity = 3
# totalMoney = 1000
# price = 450
# statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
# print(statement1.format(quantity, totalMoney, price))
