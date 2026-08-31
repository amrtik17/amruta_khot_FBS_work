#Write a program to calculate simple interest based on Principal, Rate and Time
#(SI = P*R*T/100)

P = int(input("Enter Principal amount (P): "))
T = int(input("Enter Time (T): "))
R = int(input("Enter Rate of Interest (R): "))

#calculate simple interest

SI = (P * T * R) / 100

# display result
print(f'simple interest is {SI}')