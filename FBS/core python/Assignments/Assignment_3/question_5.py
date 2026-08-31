# Write a program to check whether the triangle is equilateral, isosceles or scalene
#triangle.

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

if(a == b and b == c ):
    print('equilateral Traingle')
elif(a == b or b == c or c == a):
    print('isosceles Traingle')
else:
    print('scalene Traingle')     #scalene traingle means all side differant (a !=b and b != c and a != d)
 