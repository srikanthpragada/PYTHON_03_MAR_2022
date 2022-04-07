# Take marks from marks.txt and display total
f = open("marks.txt", "rt")
for line in f.readlines():
    if line.strip() == "":   # Blank line
        continue

    parts = line.strip().split(",")
    name = parts[0]
    marks = parts[1:]
    total = sum(map(int,marks))
    print(f"{name:10} {total:3}")

f.close()
