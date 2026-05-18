class Employee:
    language="python"
    salary=12000

    def getInfo(self):
        print(f"the language is {self.language}")

harry = Employee()
harry.language= "java"

print(harry.language,harry.salary)
harry.getInfo()