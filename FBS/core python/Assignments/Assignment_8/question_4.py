#Sum of all odd numbers between 1 to n

def sumOfOddNumber():
    sum = 0
    for i in range(1,n+1):
        if (i % 2 != 0):
            sum = sum + i
    return sum
n = int(input("Enter number: "))
res = sumOfOddNumber()
print(f'Sum of odd number is: {res}')

