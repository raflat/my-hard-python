from os.path import dirname, join


def absolute_path(relative_path):
    current_dir = dirname(dirname(__file__))
    return join(current_dir, relative_path)


def clean(list):
    return list.strip("\n").split(",")


def lists(file):
    lines = [to_int(clean(line)) for line in file.readlines()]

    return lines[0], lines[1]


def open_read(path):
    return open(absolute_path(path), "r")


def open_write(path):
    return open(absolute_path(path), "w")


def sum_matrix(list1, list2):
    matrix = [
        [x + y if pos_x == pos_y else 0 for pos_x, x in enumerate(list1)]
        for pos_y, y in enumerate(list2)
        ]

    return matrix


def to_char(list):
    return [str(num) for num in list]


def to_int(list):
    return [int(num) for num in list]


def write_matrix(file, matrix):
    for row in matrix:
        line = []

        for num in row:
            line.append(str(num))

        file.write(",".join(line) + "\n")


def main():
    with open_read(r"data\file_04_1.txt") as src_file:
        list1, list2 = lists(src_file)

    with open_write(r"data\file_04_2.txt") as dest_file:
        write_matrix(dest_file, sum_matrix(list1, list2))


if __name__ == "__main__":
    main()
