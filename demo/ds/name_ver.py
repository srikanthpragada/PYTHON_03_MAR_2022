names = ["Java", "Python", "C#", "JavaScript"]
vers = [17, 3.10, 11]

for idx, name in enumerate(names):
    if idx >= len(vers):
        ver = 'Unknown'
    else:
        ver = vers[idx]

    print(f"{name:20} {ver}")
