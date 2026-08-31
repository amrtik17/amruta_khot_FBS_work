#Write a program to accept distance in km and convert it into meters and
#centimeters both.

km = float(input("Enter distance in kilometers: "))

m = km * 1000
cm = km * 100000

print(f'Distance in meter is:{m}')
print(f'distance in centimeter is:{cm}')

