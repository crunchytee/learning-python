def add_one(input):
    return input + 1

my_tuple = (5,34,3,5,5555,4)

x = map(add_one, my_tuple)
print(x)
print(list(x))
