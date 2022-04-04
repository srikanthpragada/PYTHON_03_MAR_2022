from abc import ABC, abstractmethod


# Abstract class
class Doctor(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def show(self):
        print("Name : ", self.name)
        print("Dept : ", self.dept)

    @abstractmethod
    def get_salary(self):
        pass


class Resident(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    # Overriding show() in superclass
    def show(self):
        super().show()
        print("Salary : ", self.salary)

    def get_salary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, visits, rate):
        super().__init__(name, dept)
        self.visits = visits
        self.rate = rate

    # Overriding show() in superclass
    def show(self):
        super().show()
        print("Visits : ", self.visits)
        print("Rate   : ", self.rate)

    def get_salary(self):
        return self.visits * self.rate


r = Resident("Dr. Andy", "Ped", 500000)
r.show()

c = Consultant("Dr. James", "GP", 10, 1500)
c.show()
print(c.get_salary())
