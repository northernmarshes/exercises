#!/usr/bin/env python3
# -----task-source:-pynative.com------
# Exercise 23: Create a simple countdown timer using a while loop.
# Write a code to create a simple countdown timer of 5 seconds using a while loop.
# Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.

import time

sec = 5
while sec > 0:
    time.sleep(1)
    print (f"Time remaining: {sec} seconds")
    sec = sec-1
print ("Time's up!")

# ----------- Future Tips: -----------
# Niepotrzebne czekanie na początku,
# lepsze rozwiązanie:
# def countdown_timer(seconds):
#     while seconds > 0:
#         print(f"Time remaining: {seconds} seconds")
#         time.sleep(1)
#         seconds -= 1
#     print("Time's up!")
# countdown_timer(5)
