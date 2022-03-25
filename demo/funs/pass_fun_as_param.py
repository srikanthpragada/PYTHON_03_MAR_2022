def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def operate(func, n1, n2):
    print(func(n1, n2))


operate(add, 10, 20)
operate(multiply, 5, 10)  # User-defined function
operate(max, 5, 10)   # Built-in function

# Lambda
operate(lambda a, b: a // b, 100, 10)  # Lambda expression
