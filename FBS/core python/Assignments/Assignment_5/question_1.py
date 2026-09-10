#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

id = "ak123"
password = "12345"

count = 1

while count <= 3:
    userid = input("Enter User ID: ")
    password1 = input("Enter Password: ")

    if userid == id and password1 == password:
        print("Login successful")
        break
    else:
        print("Incorrect User ID or Password")
        count = count + 1

if count > 3:
    print(" 3 attempts completed. Program terminated.")