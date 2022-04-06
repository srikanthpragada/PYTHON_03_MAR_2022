# Take 5 numbers and display total
# Ignore invalid numbers

count = total = 0
while True:
    try:
        num = int(input("Enter number :"))
        total += num
        count += 1
        if count == 5:
            break
    except ValueError:
        print("Invalid Number!")

print(f"Total = {total}")