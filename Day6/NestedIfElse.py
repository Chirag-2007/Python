n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

if n1 > n2:
    if n1 > n3:
        print(n1, "is the greatest element")
    else:
        print(n3, "is the greatest element")
else:
    if n2 > n3:
        print(n2, "is the greatest element")
    else:
        print(n3, "is the greatest element")