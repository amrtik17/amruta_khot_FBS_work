#Write a program to calculate profit or loss.

sp = int(input('Enter Selling Price: '))
cp = int(input('Enter cost price: '))

if(sp > cp):
    # profit = sp - cp
    print('profit')

elif(sp < cp):
    # loss = cp - sp
    print('loss')
else:
    print('No profit No loss')