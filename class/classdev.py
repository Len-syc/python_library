from allclass import Student
class Bigstudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.done = 100
    def dohomework(self):
        print(self.name, "在做作业")
    def playgame(self):
        print(self.name, "的作业是:", self.age * 2)

class Smallstudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.done = False
    def dohomework(self):
        print(self.name, "在做作业")
    def playgame(self):
        print(self.name, "的作业是:", self.age * 2)
    def poop(self):
        print(self.name, "small在拉屎")


student1 =Bigstudent("大学生", 18)
print(student1.name)
print(student1.age)
student1.dohomework()
student1.playgame()
student2 = Smallstudent("小学生", 12)
print(student2.name)
print(student2.age)
student2.poop()

