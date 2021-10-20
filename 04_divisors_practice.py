user_input = int(input("Please input an integer: "))
results = []
for item in range(1, user_input+1):
    if user_input % item == 0:
        results.append(item)

print(results)

