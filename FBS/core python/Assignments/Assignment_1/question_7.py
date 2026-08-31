# Program to Find the Roots of a Quadratic Equation (-b(+-)(b**2 - 4*a*c))/2*a

a = float(input('Enter value of a : '))
b = float(input('Enter value of b : '))
c = float(input('Enter value of c : '))

d = (b ** 2) - 4 * a * c

r1 = (-b + d ** 0.5) / 2 * a
r2 = (-b - d ** 0.5) / 2 * a

print(f'Root 1 is :{r1}')
print(f'Root 2 is :{r2}')