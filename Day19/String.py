# Creating a String
name1 = 'Chirag'
name2 = "Ram"
name3 = '''Chirag is a
good boy.'''

print(name1, name2, name3)
print(name1[0])
print(name1[-1])

#Traverse a string
# for loop
for i in name1:
    print(i)

#list comprehension
list = [char for char in name1]
for i in list:
    print(i)

# length of string
print(len(name1))

#find a char/substring in a string
print(name1.find('rag'))

#Slicing a string
str = "abcdef"
output = str[2:4]
print(output)

#slice from the start
output = str[:5]
print(output)

#Slice from the end
output = str[2:]
print(output)

#negative indexing
output = str[-3:]
print(output)
