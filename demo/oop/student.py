class Student:
    courses = {"java": 15000, "python": 10000, ".net": 12500, "ds": 20000}

    @staticmethod
    def getcourses():
        return Student.courses

    @staticmethod
    def getcoursefee(course):
        return Student.courses[course]

    def __init__(self, rollno, name, course='python'):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.feepaid = 0

    def pay(self, amount):
        self.feepaid += amount

    def gettotalfee(self):
        return Student.courses[self.course]

    def getdue(self):
        return self.gettotalfee() - self.feepaid

    @property
    def totalfee(self):
        return Student.courses[self.course]


print(Student.getcoursefee(".net"))

s1 = Student(1, "Jack")
print(s1.totalfee)   # Access property
s2 = Student(2, "Bob", "java")

s1.pay(5000)
s1.pay(3000)
s2.pay(10000)

print(s1.getdue())
