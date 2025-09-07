# for converting character into uppercase
str1 = "new york"
str2 = str1.upper()
print(str2)

# for converting character into lowercase
str3 = str2.lower()
print(str3)

#for capitalising the first character a string
str4 = str2.capitalize()
print(str4)

#for stripping/removing any trailing whitespaces
str1 = "    hello world!    "
print(str1.strip())

#replacing substring
str1 = "Hello world, what a beautiful world this is!"
print(str1.replace("world","earth"))

str1 = "Hello world, what a beautiful world this is!"
print(str1.replace("world","earth",1))

# Split 
str1 = "ria pia sia tia mia"
list = str1.split()
print(list)

# Concartinate a string
str1 = "Hello World!"
str2 = "What a great place this is"
print(str1 + str2)

# formatting
student_name = "Pallavi"
student_marks = 98

str1 = "The student name is {s}, and marks is {m}".format(s = student_name, m = student_marks)
print(str1)

