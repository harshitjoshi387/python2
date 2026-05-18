class Employee:
    company="itc"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company="itc infotech"
    def showlanguage(self):
        print(f"the name is {self.name}and he is good with {self.language}")

a=Employee()
b=Programmer()

print(a.company,b.company)