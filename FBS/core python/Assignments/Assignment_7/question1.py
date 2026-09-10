n = 5

for i in range(n):
    print(" " * (n-i-1) + "*" + " " * (2*i-1) +
           "*" if i > 0 else " " * (n-i-1) + "*")

for i in range(n):
    print(" " * i + "*" + " " * (2*(n-i)-3)
           + "*" if i < n-1 else " " * i + "*")