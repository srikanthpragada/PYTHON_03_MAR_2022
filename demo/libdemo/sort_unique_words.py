import re

with open("old_man.txt", "rt") as f:
    contents = f.read()

words = set(re.findall(r"\w+", contents))

for w in sorted(words):
    print(w)
