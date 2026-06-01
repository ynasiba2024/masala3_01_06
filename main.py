#3-masala
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

e1 = Employee("Jasur", 5000)

print(e1.salary)

e1.salary = 7000
print(e1.salary)
