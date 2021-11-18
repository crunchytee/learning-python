def convert_to_set_of_ints(file):
    file_split = file.read().split()
    result = {int(item) for item in file_split}
    return result


with open("primenumbers.txt") as file1, open("happynumbers.txt") as file2:
    file1_converted = convert_to_set_of_ints(file1)
    file2_converted = convert_to_set_of_ints(file2)
    result = file1_converted.intersection(file2_converted)

print(result)
