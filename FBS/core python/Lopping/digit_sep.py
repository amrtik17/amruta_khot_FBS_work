# digit seprateout 

num = int(input('Enter naumber: '))
sum = 0
while(num > 0):
    d = num % 10
    print (d)
    sum += d
    num = num // 10
print (f'sum of all digits are :{sum}' )