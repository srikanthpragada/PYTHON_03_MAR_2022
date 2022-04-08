# Take marks from marks.txt and display total
f = open("marks.txt", "rt")
students = {}
for line in f.readlines():
    if line.strip() == "":  # Blank line
        continue

    parts = line.strip().split(",")
    name = parts[0]
    marks = parts[1:]
    valid_marks = filter(str.isdigit, marks)
    total = sum(map(int, valid_marks))
    students[name] = total

f.close()
for name, total in sorted(students.items()):
    print(f"{name:10} {total:3}")
