class Student:
    def __init__(self, name, student_id):
        self.name = name#这个name是从 def __int__(self,name）获取的
        self.student_id = student_id#和上面的一样
        self.grades = {'语文': 0, '数学': 0, '英语': 0}


    def set_grades(self,kemu,cenji):
        if kemu in self.grades:
            self.grades[kemu] = cenji

    def print_grades(self):
        print(f"学生{self.name} (学号：{self.student_id}) 的成绩为：")
        for kemu in self.grades:
            print(f"{kemu}: {self.grades[kemu]}分")

lenqing = Student('冷清', '100001')
lenqing.set_grades('数学',100)
lenqing.set_grades('英语',150)
lenqing.set_grades('语文',100)
lenqing.print_grades()