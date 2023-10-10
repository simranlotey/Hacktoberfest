i = int(input("Enter diamond's height: "))
for x in range(i):
    print(" " * (i - x), "*" * (2*x + 1))
for x in range(i - 2, -1, -1):
    print(" " * (i - x), "*" * (2*x + 1))