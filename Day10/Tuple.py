colors = ("red","yellow","green")
print(type(colors))

#length of tuple
print(len(colors))

#accessing items in a tuple
print(colors[0])
print(colors[-1])
print(colors[1:3])

#checking items exit in tuple
if "green" in colors:
    print("Green is a part of tuple")

#traverse in tuple
for i in colors:
    print(i)

# Concartinate two tuples
more_colors = ("blue","brown")
colors = colors + more_colors
print(colors)

#unpacking a tuple
color1, color2, color3 = colors
print(color1, color2, color3)