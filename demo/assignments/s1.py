st = "Java SE 17"
s = set(st)
s1 = set()
s2 = set()
s3 = set()

for c in s:
    if c.isupper():
        s1.add(c)
    elif c.islower():
        s2.add(c)
    elif c.isdigit():
        s3.add(c)

print(s1, " ")
print(s2, " ")
print(s3, " ")
