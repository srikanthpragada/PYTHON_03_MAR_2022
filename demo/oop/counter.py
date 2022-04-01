class Counter:
    def __init__(self, start=1, increment=1):
        self.counter = start
        self.inc_value = increment

    def increment(self):
        self.counter += self.inc_value

    def decrement(self):
        self.counter -= self.inc_value

    @property
    def value(self):
        return self.counter

    def __str__(self):
        return f"{self.counter}, {self.inc_value}"

    # used when object is converted to int - int(obj)
    def __int__(self):
        return self.counter

    def __eq__(self, other):
        return self.counter == other.counter and self.inc_value == other.inc_value


c = Counter(100, 5)
c2 = Counter()
c.increment()
c.increment()
print(c.value, c2.value)
print(int(c) + int(c2))
