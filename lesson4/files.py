from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, r"data\file_00.txt")

# Write in a file
lines = ["line 1", "line 2", "line 3"]
with open(path, "w") as file:
    for line in lines:
        file.write(line + "\n")

# Open a file in read mode and print its content
file = open(path, "r")
print(file.read())

# Read a file line by line
print([line for line in file])

# Close an opened file
file.close()

# Define the scope of a file and close it automatically
with open(path, "r") as file:
    file.read()
