#Numerical Approximation of 1/pi using the method of Srinivasa Ramanujan.
#Credits: The program is taken from the book of Allen Downey: Think Python 2 (2015).

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def approx_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial (4*k) * (1103 + 26390 * k)
        div = factorial(k) ** 4 * 396 ** (4*k)
        term = factor * num / div
        total += term

        if abs(term) < 1e-15:
            break
        k += 1

        return 1/total

print (approx_pi())

#this program estimates the value of pi using recursions and while loops.
