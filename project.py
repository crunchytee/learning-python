from datetime import datetime

def user_input():
    first_name = input("Please input your first name: ").capitalize()
    age = int(input("Please input your age: "))
    turns_100_in = datetime.today().year - age + 100
    print(f"{first_name}, you will be 100 in the year {turns_100_in}")

user_input()
