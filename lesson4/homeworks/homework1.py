from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, r"..\data\file_01.txt")

with open(path, "r") as file:
    lines = file.readlines()
    print("fourth line:", lines[3])
