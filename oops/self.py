class Employee:
    language="python"
    salary=12000

    def __init__(self):  #dunder method which is automatically called
        print('i am creating a object')


    def getInfo(self):
        print(f"the language is {self.language}")

    @staticmethod #static
    def greet():
        print("Good morning")

harry = Employee()
harry.language= "java"

print(harry.language,harry.salary)
harry.getInfo()
harry.greet()