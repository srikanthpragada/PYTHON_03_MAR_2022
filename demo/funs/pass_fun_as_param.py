def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def operate(func, n1, n2):
    print(func(n1, n2))


operate(add, 10, 20)
operate(multiply, 5, 10)
operate(max, 5, 10)
