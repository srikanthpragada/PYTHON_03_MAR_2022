def zero(a):
    print(id(a))
    a = 0
    print(id(a))


def prepend(lst, value):
    lst.insert(0, value)


# Immutable object
n = 10
print(id(n))
zero(n)
print(n)

# Mutable object
l = [1, 2, 3]
prepend(l, 100)
print(l)
