def unique_chars(*names):
    chars = set()
    for n in names:
        chars = chars | set(n)

    print(chars)


unique_chars("Java", "Python", "JavaScript")
