# write a functions that print hello world
def printHello():
    print("Hello World!!")
printHello()

def add(n1, n2=0):
    sum = n1 + n2
    return sum
# positional arguments
print("The sum is", add(2,3))

# Keyword argument / named argument
print("The sum is", add(n1=2,n2=3))

#default argument
print("The sum is", add(3))

#Arbitrary arguments
def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

output = addAllNumbers(2,3,4,5)
print(output)

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentInfo(name="Chirag",age=18,city="Ambala")
print()
studentInfo(name="Chennu",age=19,city="Delhi")