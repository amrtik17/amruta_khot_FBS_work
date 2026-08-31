#fibonacci series 
num = int(input('Enter fibonacci number: '))

a = -1
b = 1
for i in range(num):
    c = a + b
    print(c, end = ' ')
    a = b
    b = c