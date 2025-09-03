def outer_fucntion():
    x = 1

    def inner_function():
        y = 2
        result = x + y
        return result
    return inner_function()

output = outer_fucntion()
print(output)