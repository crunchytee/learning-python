user_input = input("Please input a string and I'll tell you whether it's a palindrome or not:")

iterator_index_forward = 0
iterator_index_backward = len(user_input) - 1
is_palindrome = False

for letter in user_input:
    if user_input[iterator_index_forward].upper() == user_input[iterator_index_backward].upper():
        iterator_index_forward += 1
        iterator_index_backward -= 1
        is_palindrome = True
    else: break
print(f"{user_input} IS a palindrome" if is_palindrome else f"{user_input} is NOT a palindrome")
