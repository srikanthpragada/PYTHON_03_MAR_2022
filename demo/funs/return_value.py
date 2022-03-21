def add(n1: int, n2: int) -> int:
    return n1 + n2

def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False
    # return  n % 2 == 0

def count_upper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count 



print(add(10, 20))
print(add("Hi", "Hello"))
# print(add(10, "Abc"))
