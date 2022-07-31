"""Lists and Dictionaries"""

# Lists
DOUBLE_NEWLINE = '\n\n'

numbers = [1, 2, 3]
print(numbers)
print(type(list))
print(len(numbers), end=DOUBLE_NEWLINE)

print(numbers[1])

numbers[2] = 30
print(numbers, end=DOUBLE_NEWLINE)

generic_list = [1, True, 3.0, "String"]

i = 0
while i < len(generic_list):
    print(generic_list[i])
    i += 1

# Dictionaries
dictionary = {"name": "Dario", "nickname": "raflat"}

print()
print(dictionary["nickname"])
print(dictionary)
print(type(dictionary))
print(len(dictionary))
print(dictionary.keys())
print(dictionary.values())
print('nickname' in dictionary.keys())

print()
for key, value in dictionary.items():
    print(key, value, sep=': ')
