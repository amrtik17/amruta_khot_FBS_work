n = 5

for i in range(1, n + 1):

    # Left side
    for j in range(1, i + 1):
        print(j, end=" ")

    # Middle spaces
    print("  " * (2 * (n - i)), end="")

    # Right side
    for j in range(i-1, 0, -1):
        print(j, end=" ")

    print()