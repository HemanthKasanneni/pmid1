n = int(input("Enter pattern size: "))
if n <= 0:
    print("Invalid size")
else:
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()