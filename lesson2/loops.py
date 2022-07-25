"""For and While loops"""

#while
condition = True

while condition:
    print("Hello!")
    condition = False

print()

count = 0
while count < 10:
    print(count)
    count += 1

print()

#for
numbers = [1, 2, 3]

for number in numbers:
    print(number)

print()

for i in range(0, 10):
    print(i, end=' ')
