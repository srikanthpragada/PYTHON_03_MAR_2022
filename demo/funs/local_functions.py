g = 1000   # Global

def f1():
    global g
    g = 1
    a = 10      # Enclosing
    print("f1()")

    # Local function
    def f2():
        nonlocal a
        a = 100
        b = 20      # Local variable
        print("f2()", a, b)

    f2()
    print(a)

f1()
