# Write a program to enter P,T, R and  calculate simple interest
# take imput P,T,R
P = int(input("Enter Principal amount (P): "))
T = int(input("Enter Time (T): "))
R = int(input("Enter Rate of Interest (R): "))

#calculate simple interest

SI = (P * T * R) / 100

# display result
print(f'simple interest is {SI}')