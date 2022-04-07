# Open names.txt and display names from it
with open("names.txt", "rt") as f:
    for line in f.readlines():
        print(line.strip())
