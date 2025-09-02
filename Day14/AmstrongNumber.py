num = int(input("Enter the number: "))
length = len(str(num))
sum = 0
original_number = num
if num > 0:
    for i in range(length):
        last_number =  num % 10
        power = last_number ** length
        sum = sum + power
        num = num//10
else:
    print("Armstrong Numbers are always positive")

if original_number == sum:
   print("Armstrong Number")
else:
   print("Not a Armstrong Number")
