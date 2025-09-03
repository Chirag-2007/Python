n = int(input("Enter the number: "))
#Function ke through
def sumOneToN(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

# call function
output = sumOneToN(n)
print("The output is:",output)