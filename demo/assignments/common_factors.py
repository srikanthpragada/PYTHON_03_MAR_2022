# common factors
num1, num2 = 10, 20

smallest = min(num1, num2)
for n in range(2, smallest // 2 + 1):
    if num1 % n == 0 and num2 % n == 0:
        print(n)
