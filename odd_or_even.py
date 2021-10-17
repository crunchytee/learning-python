user_input = input("Please input an integer: ")

try: 
    refined_user_input = int(user_input)
except ValueError:
    print("Invalid input, please try again with an integer")
    exit()

if refined_user_input % 2 == 0:
    print("Your input was an even number")
else:
    print("Your input was an odd number")