a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
operator = input("Enter the operator(+,-,*,/): ")

if operator == "+":
    output = a + b
    print("The output is: ",output)
elif operator == "-":
    output = a - b
    print("The output is: ",output)
elif operator == "*":
    output = a * b
    print("The output is: ",output)
else:
    output = a / b
    print("The output is: ",output)
    