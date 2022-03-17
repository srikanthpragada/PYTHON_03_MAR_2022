
s = "Java SE 17"

a = {c for c in s if c.isupper()}
b = {c for c in s if c.islower()}
d = {c for c in s if c.isdigit()}

print(a, b, d)
