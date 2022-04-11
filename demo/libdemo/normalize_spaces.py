import re

filename = "test.txt"
with open(filename, "rt") as f:
    contents = f.read()

newcontents = re.sub(r"[ ]+", ' ', contents)
newcontents = re.sub(r"[\n]+", '\n', newcontents)

with open(filename, "wt") as f:
    f.write(newcontents)
