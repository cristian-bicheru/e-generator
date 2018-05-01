# By Cristian Bicheru
# Supports Python 3
# Python 2 Has Some Weird Issues
############################################

from math import *
from decimal import *

print("Enter Desiered Decimal Precision:")
precision = input()

getcontext().prec = int(precision)

count = -1

e = 0

while True:
    count += 1
    d = Decimal(str(e))
    e = Decimal(str(d)) + Decimal(1 / factorial(count))
    if e == d:
        print(str(Decimal(e)))
        break
