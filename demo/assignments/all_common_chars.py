def unique_chars(*names):
    chars = set(names[0])
    for n in names[1:]:
        chars = chars & set(n)

    print(chars)


unique_chars("Kotlin", "Python", "Cobol")

