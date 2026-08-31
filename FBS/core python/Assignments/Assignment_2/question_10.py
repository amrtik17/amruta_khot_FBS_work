# Write a program to reverse three-digit number.

num = int(input('Enter number : '))

revnum1 = num % 10
num = num // 10
revnum2 = num % 10
revnum3 = num // 10

print (f'reverse three-digit number is {revnum1}{revnum2}{revnum3}')
