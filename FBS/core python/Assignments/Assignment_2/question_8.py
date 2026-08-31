# Write a program to swap two numbers using third variable.

a = int(input('Enter number: '))
b = int(input('Enter number: '))

print(f'before swapping a: {a} b: {b}')

c = a
a = b
b = c

print(f'After swapping a : {a} b: {b}')
