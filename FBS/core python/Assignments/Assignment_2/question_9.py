# Write a program to swap two numbers without using third variable.

a = int(input('Enter Number : '))
b = int(input('Enter Numbers : '))
print(f'before swapping a : {a} b : {b}')

a = a + b
b = a - b
a = a - b

print(f'After swapping is: a: {a} b : {b}')