names = ["Java", "Python", "C#", "JavaScript"]
vers = [17, 3.10, 11]

# for idx, name in enumerate(names):
#     print(name, vers[idx])

for name, ver in zip(names, vers):
    print(name, ver)
