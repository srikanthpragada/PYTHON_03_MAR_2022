# Take names until end and display avg. length

total = 0
count = 0
while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    total += len(name)
    count += 1

print('Average length = ',total//count)
