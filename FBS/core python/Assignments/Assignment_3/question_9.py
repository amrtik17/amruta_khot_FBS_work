#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input("Enter 1st subject marks: "))
sub2 = int(input("Enter 2nd subject marks: "))
sub3 = int(input("Enter 3rd subject marks: "))
sub4 = int(input("Enter 4th subject marks: "))
sub5 = int(input("Enter 5th subject marks: "))

per = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if(per > 75):
    print('First class')
elif(per > 60):
    print('second class')
elif(per > 50):
    print('Third class')
elif(per > 39):
    print('pass')
else:
    print('fail')


