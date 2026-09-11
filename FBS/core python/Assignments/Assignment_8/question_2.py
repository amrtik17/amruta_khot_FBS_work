#Write a program to calculate area of circle

import math


def areaOfCircle(r):
    area = math.pi * r**2
    return area
r = float(input(("Enter radius: ")))
res = areaOfCircle(r)
print(f'Area of circle is : {res}')