#!/usr/bin/env python3
import time

"""moje rozwiązanie"""
sec = 5
while sec > 0:
    time.sleep(1)
    print (f"Time remaining: {sec} seconds")
    sec = sec-1
print ("Time's up!")

"""Niepotrzebne czekanie na początku,
lepsze rozwiązanie:"""

# def countdown_timer(seconds):
#     while seconds > 0:
#         print(f"Time remaining: {seconds} seconds")
#         time.sleep(1)
#         seconds -= 1
#     print("Time's up!")

# countdown_timer(5)
