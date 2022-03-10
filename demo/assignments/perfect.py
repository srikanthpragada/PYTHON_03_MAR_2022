num = int(input("enter a number:"))
sum = 0
for n in range(1, num // 2 + 1):
    if num % n == 0:
        sum = sum + n

if sum == num:
    print("it is a perfect number")
else:
    print("it is not a perfect number")
