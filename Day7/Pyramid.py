n = int(input("Enter n : "))

for i in range(1, n+1): # loops for rows
    # printing spaces
    print(" " * (n-i), end="")

    # print digits
    for j in range(1, (2*i-1) + 1):
        print(j, end="")
    print()