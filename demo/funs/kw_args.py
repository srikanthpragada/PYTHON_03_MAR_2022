def print_details(**kwargs):
    print(kwargs)


def fun(*args, **kwargs):
    pass


print_details(name="Scott", age=30)
print_details(title="Outlier", author="Gladwell")

fun(10, 20, x=1, y=20)
