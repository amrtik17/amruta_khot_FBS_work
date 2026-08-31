#Calculate the cost of painting the following building’s walls (both interior and
#exterior). You need to accept area (one wall) and cost of both interior and
#exterior wall.



area = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter cost:  "))
exterior_cost = float(input("Enter cost : "))

area_interior = 8 * area


area_exterior = 6 * area

total_i = area_interior * interior_cost
total_e = area * exterior_cost

total_cost = total_i + total_e

print(area_interior)
print(area_exterior)
print(total_i)
print(total_e)
print( total_cost)