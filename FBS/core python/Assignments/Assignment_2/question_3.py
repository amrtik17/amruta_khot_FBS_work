# Convert distant given in feet and inches into meter and centimeter.

feet = float(input('Enter distance in feet : '))
inches = float(input('Enter distance in inches : '))

total_inches = (feet * 12) + inches

Meter = total_inches * 0.0254
Centimeter = Meter * 100

print(f'Distance in Meter is : {Meter}')
print(f'Distance in centimeter is : {Centimeter}')