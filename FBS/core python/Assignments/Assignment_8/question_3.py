#Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

# a. 1+ 2 + 3 + 4+..... + n

def sumOfSeries():
    sum = 0
    for i in range (1, n+1):
        sum = sum + i
    return sum
n = int(input("Enter number: "))
res = sumOfSeries()
print(res)

#b. 1!+ 2! + 3! + 4!+..... + n!

def factorial(n):
    sum = 0
    fact = 1
    
    for i in range(1,n+1):
        fact = fact * i
        sum = sum + fact
    return sum

n = int(input("Enter number: "))
res = factorial(n)
print(f' factotial of given number is {res}')

#c. 1^1 + 2^2 + 3^3+ ...... n^n
def powerOfNumber():
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i**i
    return sum
n = int(input("Enter number: "))
res = powerOfNumber()
print(f' sum of number power is: {res}')
 