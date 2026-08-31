#Write a program to prompt user to enter userid and password. After verifying userid and password
#  display a 4 digit random number and ask user to enter the same. If user enters the same number 
# then show him success message otherwise failed. (Something like captcha)

import random
userId = input('Enyer used id: ')
password = input('Enter password: ')
if userId == "ak@123" and password == "Aa9696":
    systemCapcha = random.randint(1000,10000)
    print(systemCapcha)
    captcha = int(input('Enter the captcha: '))
    if captcha == systemCapcha:
        print("successfully log in")
    else:
        print("Invalid Id and Password..")