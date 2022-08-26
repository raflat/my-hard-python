# Let's now look close at how Python handles and interprets the code.
# How some code is interpreted can be seen by using this website:
# https://pythontutor.com/render.html

# Two areas of memory:
# 1. Stack:
#    - contains variables.
#    - elements are placed and taken only from the top.
#    - has a fixed size.
#    - only specific portions are available, these portions are called frames.
#      This concept defines the scope of a certain variable.
#    - variables contained here can point to areas in the heap.
# 2. Heap:
#    - contains objects, so pointers.
#    - has no fixed size.

# Code snippets to analyze:

# 1)
a = 10
b = 15
c = a + b

# 2)
li = [1, 2, "something"]
d = {"id": 100, "username": "enkk"}
ld = {"id": 100, "username": "enkk",
      "friends": ["studytme", "homyatol", "trump"]}

ld["friends"].append("obama")

other_friends = ["panetty", "violet"]
ld["friends"] = other_friends

# 3)
li = ["a", "b", "c", "d"]

# 4)
for i in range(len(li)):
    print(li[i])

# 5)
for elem in li:
    elem = "z"

# 6)
li = [["a"], ["b"], ["c"], ["d"]]

# 7)
for elem in li:
    new_elem = ["z"]
    elem = new_elem

# 8)
for elem in li:
    elem[0] = "z"
