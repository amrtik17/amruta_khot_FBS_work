#Write a program to input any alphabet and check whether it is vowel or consonant.

char = input("Enter an alphabet: ")

if char in "aeiouAEIOU":
    print("It is a vowel")
else:
    print("It is a consonant")