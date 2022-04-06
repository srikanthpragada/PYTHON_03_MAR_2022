def numbers():
    for n in range(1, 6):
        yield n


def codes(st):
    for c in st:
        yield ord(c)


nums = numbers()
print(type(nums))
print(next(nums))
print(next(nums))

for n in codes("axy"):
    print(n)