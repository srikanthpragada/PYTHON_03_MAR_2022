def nonblank(s):
    for c in s:
        if not c.isspace():
            print(c, end='')


nonblank("This is okay")
