"""List comprehension"""

# Without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for f in fruits:
    if "a" in f:
        new_list.append(f)

print(new_list)

# With list comprehension
new_list = [f for f in fruits if "a" in f]
print(new_list)

# List comprehensions syntax: list = [expression for item in iterable if condition]

# Examples
new_list = [f for f in fruits if f != "apple"]
print(new_list)

new_list = [f for f in fruits]
print(new_list)

new_list = [x for x in range(10)]
print(new_list)

new_list = [x for x in range(10) if x < 5]
print(new_list)

new_list = [f.upper() for f in fruits]
print(new_list)

new_list = [f if f != "banana" else "orange" for f in fruits]
print(new_list)
