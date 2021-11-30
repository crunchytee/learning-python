import file_overlap_23


class TestClass:
    def test_convert_to_set_of_ints(self):
        testing_file = "primenumbers.txt"
        with open(testing_file) as testing_file:
            converted_file = file_overlap_23.convert_to_set_of_ints(
                testing_file)
        assert type(converted_file) == type(set())
        assert len(converted_file) == 168
        for num in converted_file:
            assert type(num) == int

    def test_intersection_of_two_files(self):
        testing_file1 = "primenumbers.txt"
        testing_file2 = "happynumbers.txt"
        result = file_overlap_23.intersection_of_two_files(
            file_overlap_23.convert_to_set_of_ints, testing_file1, testing_file2)
        assert type(result) == type(set())
        # Would it be a good idea to do the intersection calculation manually and see that it matches?
