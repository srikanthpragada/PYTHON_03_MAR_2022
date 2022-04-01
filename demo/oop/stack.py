class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    @property
    def length(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def clear(self):
        self.data.clear()

    def __str__(self):
        return str(self.data[::-1])

    def __eq__(self, other):
        return self.data == other.data


s = Stack()
s2 = Stack()
s.push(10)
s.push(20)
s2.push(10)
s2.push(20)
print(s == s2)
print(s)
print(s.peek())
print(s.pop())
s.clear()
print(s.length, s.isempty())


