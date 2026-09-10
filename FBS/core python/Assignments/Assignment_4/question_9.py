#WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter starting number: "))
stop = int(input("Enter stop number: "))
n = int(input("Enter number to divide by: "))

for i in range(start, stop + 1):
    if i % n == 0:
        print(i)