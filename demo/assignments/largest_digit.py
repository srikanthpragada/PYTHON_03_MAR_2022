
def largest_digit(n):
    ld = 0
    while n > 0:
        d = n % 10  # take rightmost digit
        if d > ld:
            ld = d
        n = n // 10  # remove rightmost digit 

    return ld

print(largest_digit(1253))