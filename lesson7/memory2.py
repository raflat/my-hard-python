# Going deeper into understanding the visualization of memory's state during
# the execution of python programs.

# 9)
def sum(a, b):
    c = a + b
    a = 100
    b = 150

    return c


a = 10
b = 15
c = sum(a, b)

# 10)
l1 = [1, 2, 3]
l2 = [10, 20, 30]


def sum(l1, l2):
    l3 = [0]*len(l1)

    for i in range(len(l1)):
        l3[i] = l1[i]+l2[i]

    return l3


lresult = sum(l1, l2)
print(lresult)


# 11)
l1 = [1, 2, 3]
l2 = [10, 20, 30]


def sommetta(l1, l2):
    for i in range(len(l1)):
        l1[i] = l1[i] + l2[i]

    return l1


lresult = sommetta(l1, l2)
print(lresult)

# 12)
ls = ["a", "b", "c", "d"]

lc = [x for x in ls]
