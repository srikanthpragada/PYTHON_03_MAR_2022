st = "Python 3.10 is Awesome"

upper = {c for c in st if c.isupper()}
lower = {c for c in st if c.islower()}
digit = {c for c in st if c.isdigit()}

print(upper, lower, digit)
