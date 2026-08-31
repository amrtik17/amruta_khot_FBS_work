#write a program to enter P, T, R and calculate compound interest

# take imput P,T,R
P = int(input("Enter Principal amount (P): "))
T = int(input("Enter Time (T): "))
R = int(input("Enter Rate of Interest (R): "))

# calculate compound interest
CI = P * (1 + R / 100) ** T - P

# Display result
print("Compound Interest =", CI)