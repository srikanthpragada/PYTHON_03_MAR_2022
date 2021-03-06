class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Returns a string for object
    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        # print("__eq__")
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age


p1 = Person("Scott", 30)
p2 = Person("Mike", 25)
p3 = Person("Scott", 30)

print(p1)  # str(p1) ->  p1.__str__()
print(p1 == p3)
print(p1 != p2)
print(p1 > p2)
