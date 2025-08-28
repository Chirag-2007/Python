#creating a set
names = {"Sia","Hia","Tia"}
print(names)

#checking of length
length = len(names)
print(length)

#checking datatype of set
print(type(names))

#accesing items in a set
for x in names:
    print(x)

#checking items exist in a set
if "Sia" in names:
    print("yes")

#Add elements in set
names.add("Ria")
print(names)

##Add another sequence in a set
names_list = ["Ria","kia"]
names.update(names_list)
print(names)

#Removing element from a set
names.remove("Tia")
print(names)

#Join 2 sets
s1 = {'a','b','c'}
s2 = {'d','e','a'}

s3 = s1.union(s2)
print(s3)

#Keeping only duplicate while joining
s1.intersection_update(s2)
print(s1)

#Keeping all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)
