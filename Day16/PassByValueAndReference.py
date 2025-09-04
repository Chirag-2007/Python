# Pass by value
def addOne(x):
    x = x + 1
    print("Inside Function:",x)

x = 5
addOne(x)
print("Outside function:",x)

# Pass by reference
def modifyList(list):
    list.append(4)
    print("Inside function:",list)

list = [1,2,3]
modifyList(list)
print("Outside function:",list)

