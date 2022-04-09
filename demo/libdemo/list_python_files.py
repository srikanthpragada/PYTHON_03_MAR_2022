import os

entries = os.walk(r"d:\classroom\mar3\demo")
count = 0
for (dirname, dirs, files) in entries:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
            count += 1


print("Count = ", count)
