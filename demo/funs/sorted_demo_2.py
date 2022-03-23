names = ["Java", "C", "JavaScript", "SQL", "TypeScript", "Go"]

for n in sorted(names, key=len, reverse=True):
    print(n)
