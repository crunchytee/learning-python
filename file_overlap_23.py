def convert_to_set_of_ints(file):
    file_split = file.read().split()
    result = {int(item) for item in file_split}
    return result


def intersection_of_two_files(convert_to_set_of_ints, file1_name, file2_name):
    with open(file1_name) as file1, open(file2_name) as file2:
        file1_converted = convert_to_set_of_ints(file1)
        file2_converted = convert_to_set_of_ints(file2)
        result = file1_converted.intersection(file2_converted)
    return result


result = intersection_of_two_files(
    convert_to_set_of_ints, file1_name="primenumbers.txt", file2_name="happynumbers.txt")

print(result)
