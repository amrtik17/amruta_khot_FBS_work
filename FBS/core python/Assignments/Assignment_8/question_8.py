#Write a program find reverse of a number

def reverseNumber(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse


n = int(input("Enter number: "))

res = reverseNumber(n)

print(f"Reverse of number is: {res}")