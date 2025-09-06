def power(a,b):
    if b == 0:
        return 1
    ans = a * power(a,b-1)
    return ans

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(power(a,b))
