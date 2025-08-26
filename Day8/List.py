fruits = ["apple","mango","banana","cherry"]

print(type(fruits)) # for checking the type
print(fruits)
print(len(fruits)) # For length

# checking if the item is present in the list

if "banana" in fruits:
    print("Banana is the part of the list")
if "kiwi" not in fruits:
    print("Kiwi is not part of list")

# indexing in list

print(fruits[1])
print(fruits[-3])
print(fruits[1:3])
print(fruits[-3:-1])

# addding elemnt to a list

fruits.append("kiwi")
fruits.insert(2, "kiwi")
more_fruits = ["kiwi","papaya"]
fruits.extend(more_fruits)
print(fruits)

# remove element from the list

fruits.remove("banana")
fruits.pop()
print(fruits)

# changing/updating items in a list

fruits[1] = "kiwi"
fruits[1:3] = ["kiwi","papaya"]
print(fruits)
