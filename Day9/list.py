# Sorting a list
fruits = ["apple","banana","mango","cherry"]
fruits.sort() # by default ascending order 
print(fruits)
fruits.sort(reverse=True) # descending order
print(fruits)

# list comprehension
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

# copy a list
new_fruits = fruits.copy()
print(new_fruits)

# concartinate a list
new_fruits = fruits + new_fruits
print(new_fruits)

#nested list
fruits.insert(2, ["kiwi","papaya"])
print(fruits)
print(fruits[2][0])