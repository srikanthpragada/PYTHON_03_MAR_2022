def has_upper(s):
    for c in s:
        if c.isupper():
            return True

    return False


def has_digit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


# Testing - run this code only when invoked as script
if __name__ == '__main__':
    print(count_upper("Abc"))
    print(has_digit("233"))
