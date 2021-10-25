user_input = input("Please input a string and I'll tell you whether it's a palindrome or not: ")

def is_palindrome(user_input):
    # First take
    iterator_index_forward = 0
    iterator_index_backward = len(user_input) - 1

    for letter in user_input:
        if user_input[iterator_index_forward].upper() == user_input[iterator_index_backward].upper():
            iterator_index_forward += 1
            iterator_index_backward -= 1
        else: 
            print("User input is NOT a palindrome")
            return False
    print("User input IS a palindrome")
    return True

is_palindrome(user_input)
# print(f"{user_input} IS a palindrome" if user_input.upper() == user_input[::-1].upper() else f"{user_input} is NOT a palindrome")
# if user_input.upper() == user_input[::-1].upper():
#     print(f"{user_input} IS a palindrome")
# else:
#     print(f"{user_input} is NOT a palindrome")
