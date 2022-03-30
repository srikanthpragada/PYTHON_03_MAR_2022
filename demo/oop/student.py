class Student:
    def __init__(self, rollno, name, course='python'):
        self.rollno = rollno
        self.name = name
        self.course = course
        self.feepaid = 0

    def pay(self, amount):
        self.feepaid += amount

    def getdue(self):
        totalfee = 15000 if self.course == 'java' else 10000
        return totalfee - self.feepaid


s1 = Student(1, "Jack")
s2 = Student(2, "Bob", "java")

s1.pay(5000)
s1.pay(3000)
s2.pay(10000)

print(s1.getdue())
