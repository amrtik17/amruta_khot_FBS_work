#Write a program to calculate area of rectangle

def areaOfRectangle(l,b):
    area = l * b
    return area

l = int(input("Enter length: "))
b =  int (input("Enter breadth: "))

result = areaOfRectangle(l, b)
print(result)