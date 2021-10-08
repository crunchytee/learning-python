def make_upper_case(name):
    return name.upper()

if __name__ == "__main__":
    name = "sparrow"
    name_upper = make_upper_case(name)
    print(f"upper case: {name_upper}")