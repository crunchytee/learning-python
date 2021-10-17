my_tuple = ("hello", "world", "today")

enumerated_tuple = enumerate(my_tuple)

# print(enumerated_tuple)
# print(list(enumerated_tuple))
my_long_tuple = [("1","1.1","1.2"), ("2","2.1","2.2")]

for i, item, third in my_long_tuple:
    print(i)
    print(item)
    print(third)