#!/usr/bin/env python3
# Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below

income = int(input('What is your income?\n'))

def income_tax():
    if income < 10000:
        print ('Your income tax is 0')
    elif income > 10000 and income <= 20000:
        tax_1 = (income - 10000) * 0.1
        print (f"Your income tax is {tax_1}.")
    else:
        tax_2 = 1000 + ((income - 20000) * 0.2)
        print (f"Your income tax is {tax_2}.")

income_tax()

# ----------- Future Tips: -----------
