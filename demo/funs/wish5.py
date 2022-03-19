def wish(*names, msg="Hi"):
    for n in names:
        print(msg, n)


wish("Scott", "Mark", "Jack", msg="Hello")
wish("Steve", "Roberts")
