from os.path import dirname, join


def absolute_path(relative_path):
    current_dir = dirname(dirname(__file__))
    return join(current_dir, relative_path)


def open_read(path):
    return open(path, "r")


def open_write(path):
    return open(path, "w")


def list_lines(file):
    return [line.strip("\n") for line in file.readlines()]


def common_lines_file(path1, path2):
    path3 = absolute_path(r"data\file_03_3.txt")

    file1 = open_read(path1)
    file2 = open_read(path2)
    file3 = open_write(path3)

    lines1 = list_lines(file1)
    lines2 = list_lines(file2)
    file3.writelines([line + "\n" for line in lines1 if line in lines2][::-1])

    file1.close()
    file2.close()
    file3.close()


def main():
    path1 = absolute_path(r"data\file_03_1.txt")
    path2 = absolute_path(r"data\file_03_2.txt")
    common_lines_file(path1, path2)


if __name__ == "__main__":
    main()
