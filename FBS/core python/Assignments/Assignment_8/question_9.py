#Write a program to check if entered number is a palindrome or not.

def palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return True
    else:
        return False


n = int(input("Enter number: "))

res = palindrome(n)

if res:
    print("Number is palindrome")
else:
    print("Number is not palindrome")