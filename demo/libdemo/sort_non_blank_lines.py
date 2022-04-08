# Open names.txt and display names from it
with open("names.txt", "rt") as f:
    lines = []
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:  # non-blank
            lines.append(line)

    for line in sorted(lines):
        print(line)

