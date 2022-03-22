def prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False

    return True


print(prime(11), prime(25), prime(39349381))



