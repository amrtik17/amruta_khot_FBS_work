#Write a program to check if user has entered correct userid and password.

userid = "ak123"
password = "1234"

userid1 = input('Enter userid : ')
password1 = input('Enter password : ')

if(userid == userid1 and password == password1):
    print('userid and password is correct ')

else:
    print('userid and passoward is wrong')
