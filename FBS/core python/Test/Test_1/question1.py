#Write a program to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:
l = float(input('Enter length: '))
b = float(input('Enter breadth: '))
r = float(input('Enter breadth: '))
pi = 3.14

rectangle_area = l * b
semicircle_area = (pi * r **2) / 2

total_area = rectangle_area + semicircle_area

rectangle_perimeter = l + l + b

semicircle_perimeter = pi * r

total_perimeter = rectangle_perimeter + semicircle_perimeter

print(f'Area of half circle reactacngle is:{total_area}')
print(f'perimeter of half circle reactacngle is:{total_perimeter}')

