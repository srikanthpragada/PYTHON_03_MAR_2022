nums = [-10, 10, 45, -50, 98, -10]

def ispositive(n) -> bool:
    return n > 0


for n in filter(ispositive, nums):
    print(n)
