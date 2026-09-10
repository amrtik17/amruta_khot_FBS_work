#WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start = int(input("Enter start number: "))
stop = int(input("Enter stop number: "))

for i in range(start, stop + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)