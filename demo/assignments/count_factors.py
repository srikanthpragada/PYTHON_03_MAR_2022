# Count Factors for the given number
num = int(input("Enter a number : "))

count = 0
for n in range(2, num // 2 + 1):
    if num % n == 0:
         count += 1

print(f"No. of factors = {count}")