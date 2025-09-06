def fibonacci(n):
    if n == 1: # Base Case
        return 0
    elif n == 2: # Base Case
        return 1
    else: 
        return (fibonacci(n-1) + fibonacci(n-2)) # Recursive Case
    
n = int(int(input("Enter n: ")))
for i in range(1, n+1):
    print(fibonacci(i))

