import pathlib

data_path = "test.txt"
new_file_data_path = "new_test.txt"


def read_and_cut_lines(path, line_numbers):
    with open(path, "r") as test_file:
        return list([line.replace("\n", "") for line in test_file.readlines()])[:line_numbers]


def write_lines_to_file(path_to_save, data):
    new_filename = pathlib.Path(path_to_save).stem + "_res"
    file_extension = pathlib.Path(path_to_save).suffix
    new_path = new_filename + file_extension
    cleared_data = list([line.replace("|", " ") for line in data])

    with open(new_path, "w") as test_file:
        test_file.write("\n".join(cleared_data))
    return new_path


def read_cut_write_lines(origin_path, number_of_lines_to_cut, path_to_save):
    data = read_and_cut_lines(origin_path, number_of_lines_to_cut)
    return write_lines_to_file(path_to_save, data)


print(read_cut_write_lines(data_path, 10, new_file_data_path))
