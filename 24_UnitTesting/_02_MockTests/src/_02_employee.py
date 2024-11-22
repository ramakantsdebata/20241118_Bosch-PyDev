class Employee:
    __empCount = 0

    def __init__(self, eid=None, name=None, salary=None):
        if eid is not None:
            self.eid = eid
            self.name = name
            self.salary = salary
            Employee.__empCount += 1

    @classmethod
    def getCount(cls):
        return cls.__empCount

    def getSalary(self):
        return self.salary

    def __str__(self):
        print(f"eid: {self.eid}\nname: {self.name}\n salary: {self.salary}")

class Organisation:
    def __init__(self, employees:list):
        self.employees = list(employees)
        self.high_employee = 1000
        self.low_employee = 100

    def addEmp(self, emp:Employee):
        self.employees.append(emp)

    def rmEmp(self, emp:Employee):
        self.employees.remove(emp)

    def getEmpCount(self):
        return len(self.employees)

    def checkEmployeeStrength(self):
        count = self.getEmpCount()
        if count > self.high_employee:
            return 'Too congested'
        elif count < self.low_employee:
            return 'Waste of space'
        else:
            return 'Just about right'

if __name__ == "__main__":
    emp1 = Employee(1, "Ramakant", 500)
    emp2 = Employee(2, "Manish", 400)
    emp3 = Employee(3, "Abhijeet", 300)
    org = Organisation([emp1, emp2, emp3])
    print(org.checkEmployeeStrength())
    print(org.getEmpCount())
