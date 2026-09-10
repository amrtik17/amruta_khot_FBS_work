#Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms


#a 1! + 2! + 3! + 4! + .....n!
n = int(input("Enter n: "))

fact = 1
sum = 0

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + fact

print("Sum =", sum)

#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + n ** i

print("Sum =", sum)

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter number of terms: "))

term = 1
sum = 0

for i in range(1, n + 1):
    sum = sum + term
    term = term * 2

print("Sum =", sum)

# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter a: "))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("Sum =", sum)

# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(1, n + 1):

    term = (x ** i) / (2 * i - 1)

    if i % 2 == 0:
        sum = sum - term
    else:
        sum = sum + term

print("Sum =", sum)