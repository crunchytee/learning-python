example_list = [6,7,29,35,55,4,1,12098109]

# results = []

# for item in example_list:
#     if item < 10:
#         results.append(item)

# print(results)

# print(filter())

# def my_func(input):
#     return input < 10

# my_lambda = lambda input: input < 10

# my_lambda2 = lambda input: input + 2

print(list(filter(lambda item: item < 10, example_list)))

print(list(map(lambda item: item * 2, example_list)))
