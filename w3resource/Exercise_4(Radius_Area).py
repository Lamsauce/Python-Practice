"""
===== EXERCISE #4 =====
Write a Python program which accepts the radius of a circle from the user and compute the area.

Sample Output :
r = 1.1
Area = 3.8013271108436504

"""

import decimal
from math import pi

pi = decimal.Decimal(pi)
radius = decimal.Decimal(input("Input a radius:\nRADIUS: "))
area = pi * (radius * radius)
print(area)


"""
===== RESOURCE(S) =====
https://docs.python.org/3/library/decimal.html

"""