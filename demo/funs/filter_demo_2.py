names = ["java", "Python", "c", "JavaScript", "SQL"]


def hasupper(s):
    for c in s:
        if c.isupper():
            return True

    return False


for n in filter(hasupper, names):
    print(n)


str.isdigit("233")
