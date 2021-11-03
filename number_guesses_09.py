import random

random_number = random.randint(1,9)
num_guesses = 0
user_guess = -1

while user_guess != "exit" and user_guess != random_number:
    user_guess = int(input("Please input an integer, or type exit to exit the program: "))
    num_guesses += 1
    if user_guess > random_number:
        print("Number is too high! Try again")
    elif user_guess < random_number:
        print("Number is too low! Try again")
    else:
        print(f"That's the number!! You tried {num_guesses} times.")
        
