class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.eye = 2
    def speak(self):
        print(self.name, "在说话")
    def poop(self):
        print(self.name, "在拉屎")
#有关学生的父类


class Restaurant():#res.py的父类
    def __init__(self, name, shop_type):
        self.name = name
        self.shop_type = shop_type
    def shop_restaurrant(self):
        print(f"你的名字是:{self.name}")
        print(f"你的餐厅type是:{self.shop_type}")
    def open_res(self):
        print(f"{self.name}正在营业中")

