#Write a program to find sum of digits of a number.

def sumOfDigits(n):
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10

    return sum


n = int(input("Enter number: "))

res = sumOfDigits(n)

print(f"Sum of digits is: {res}")