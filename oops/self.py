class Employee:
    language="python"
    salary=12000

    def __init__(self,name,salary,language):  #dunder method which is automatically called
        self.name=name
        self.salary = salary
        self.language = language
        print(f"{name}{salary}{language}")


    def getInfo(self):
        print(f"the language is {self.language}")

    @staticmethod #static
    def greet():
        print("Good morning")

harry = Employee("harry",12000,"javascript")
# harry.language= "java"

# print(harry.language,harry.salary)
# harry.getInfo()
# harry.greet()