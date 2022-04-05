
s = "10"
try:
    num = int(s)
    print(100 / num)
except ValueError:
    print("Sorry! Invalid Number!")
except ZeroDivisionError:
    print("Sorry! Zero is not allowed!")


print("The End")