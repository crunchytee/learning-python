def get_input():
    try:
        return int(input("Fibonacci Generator here, how many numbers would you like? Please input an integer: "))
    except ValueError:
        print("An integer I said!")
    
def generate_fibonacci():
    results = [1, 1]
    last_number = 0
    input = get_input()

    if input > 1:
        for num in range(1, input):
            results.append(results[num] + results[num - 1])
        
    print(f"Here's your numbers: {results}")

generate_fibonacci()