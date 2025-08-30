#creating a dictionary
phones = {
    "John": 98765434,
    "Ria": 738738292,
    "Joy": 4332322222
}
print(phones)

#checking type of dictionary
print(type(phones))

# checking the length
print(len(phones))

#accessing items in dictionary
print(phones["John"])

print(phones.keys())

#update value in dict
phones["John"] = 546372829
print(phones)

#Add elements in dict
phones["Kia"] = 3214322
print(phones)

more_phones = {
    "kia": 453727
}

#remove elements
phones.pop("John")
print(phones)

phones.popitem() # this will remove the last added item
print(phones)

phones.clear() # this will empty the dictionary

#printing elements of a dict
for x,y in phones.items():
    print(x,y)

#nested dictionary
phones = {
    "Area1": {
        "x":0,
        "y":1,
        "z":2
    },
    "Area2":{
        "x":3,
        "y":4,
        "z":5
    }
}
print(phones["Area1"]["y"])