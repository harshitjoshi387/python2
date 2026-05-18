class Employee:
    company="itc"
    salary=120000
    def show(self):
        print(f"the name is {self.company} and the salary is {self.salary}")

class Coder:
    language ="python"
    def printLanguage(self):
        print("out of all the language here is your language:{self.language}")

class Programmer(Employee,Coder):
    company="itc infotech"
    def showlanguage(self):
        print(f"the name is {self.company}and he is good with {self.language}")

a=Employee()
b=Programmer()


b.show()
b.showlanguage()