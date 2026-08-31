# Find the sum of three-digit number.

num = int(input('Enter three digit number : '))

a = num  // 100
num = num % 100
b = num // 10
c = num % 10

sum = a + b + c

print('addition of tree digit number is:', sum)