#!/usr/bin/env python3
# Exercise: 19: Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).

def isprime(limit):
    primes = []
    for n in range (2, limit+1):
        prime = True
        for divider in range (2, int(n**0.5) + 1):
            if n % divider == 0:
                prime = False
                break
        if prime:
            primes.append(n)
    strPrimes = ', '.join(map(str,primes))
    print (f"All prime numbers from 1 to {limit}: {strPrimes}")
    del primes[::2]
    strAltPrimes = ', '.join(map(str,primes))
    print (f"Alternate prime numbers from 1 to {limit}: {strAltPrimes}")

isprime(20)

# ----------- Future Tips: -----------
# Kod bez poprawek:
#
# def isprime(limit):
#     primes = []
#     for n in range (limit+1):
#         prime = True
#         if n == 2:
#             primes.append(n)
#         for divider in range (2, n):
#             if n % divider == 0:
#                 prime = False
#             if prime and n not in primes:
#                 primes.append(n)
#     strPrimes = ', '.join(map(str,primes))
#     print (f"All prime numbers from 1 to {limit}: {strPrimes}")
#     del primes[::2]
#     strAltPrimes = ', '.join(map(str,primes))
#     print (f"Alternate prime numbers from 1 to {limit}: {strAltPrimes}")
# isprime(20)
