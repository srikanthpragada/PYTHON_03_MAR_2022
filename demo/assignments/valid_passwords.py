def is_valid_password(pwd):
    upper = digit = special = False
    for c in pwd:
        if c.isupper():
            upper = True
        elif c.isdigit():
            digit = True
        elif c in '#@*':
            special = True

    return upper and digit and special


passwords = ["A123*45", "acb123", "##123A", "Abc_123"]

for p in filter(is_valid_password, passwords):
    print(p)
