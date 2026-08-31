#Write a program to check if given 3 digit number is a palindrome or not.

num = int (input('Enter number : '))

first = num // 100
last = num % 10

if first == last:
    print("Number is palindrome")
else:
    print("Number is not palindrome")