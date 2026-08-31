# Write a program to input angle from user and find third angle of the triangle

Angle1 = int(input("Enter 1st angle: "))
Angle2 = int(input("Enter 2nd angle: "))

Angle3 = 180 - (Angle1 + Angle2)

print(f'Third angle of traingle is : {Angle3}')

