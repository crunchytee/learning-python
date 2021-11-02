def get_divisors(input):
    divisors = []
    for num in range(2, input):
        if input % num == 0:
            divisors.append(num)
    return divisors

def is_number_prime(input):
    divisors = get_divisors(input)
    if divisors == []:
        return True
    else:
        return False

def get_int_input():
    try:
        return int(input("Please input an integer: "))
    except ValueError:
        print("Oh dude, that is not an integer.")

input = get_int_input()
bad_numbers = [0, 1]
if input not in bad_numbers and is_number_prime(input):
    print(f"your number {input} is a prime number! What are the chances!?")
else:
    print("Epic fail! That’s no prime number")

