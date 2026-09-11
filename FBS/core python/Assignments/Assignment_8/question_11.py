#WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def countDigits(n):
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10

    return count


def armstrongNumber(n):
    original = n
    digits = countDigits(n)
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** digits
        n = n // 10

    if sum == original:
        return True
    else:
        return False


n = int(input("Enter number: "))

res = armstrongNumber(n)

if res:
    print("Armstrong number")
else:
    print("Not an Armstrong number")