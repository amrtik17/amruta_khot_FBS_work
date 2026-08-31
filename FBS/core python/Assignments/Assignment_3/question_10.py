#Write a program to check if person is eligible to marry or not (male age >=21 and
#female age>=18)

gender = input('Enter Gender:(M/F) : ')
age = int (input('Enter age : '))

if(gender == 'F'):
    if(age > 18):
        print('girl Eligiblr for marriage')
    else:
        print('girl Not Eligiblr for marriage')

else:
    if(age > 21):
        print(' boy Eligiblr for marriage')
    else:
        print(' boy not Eligiblr for marriage')