from allclass import Restaurant
"""class Restaurant():
    def __init__(self, name, shop_type):
        self.name = name
        self.shop_type = shop_type
    def shop_restaurrant(self):
        print(f"你的名字是:{self.name}")
        print(f"你的餐厅type是:{self.shop_type}")
    def open_res(self):
        print(f"{self.name}正在营业中")"""#父类的属性
class Icecreamstand(Restaurant):
    def  __init__(self, name, flavors):
        super().__init__(name, "甜品")
        self.flavors = flavors
    def show_flavors(self):
        print(f"{self.name}有的类别是\n", self.flavors)


sosweet = Icecreamstand("sosweet", ["哈密瓜", "西瓜", "芝士", "巧克力"])
sosweet.shop_restaurrant()
sosweet.show_flavors()
sosweet.open_res()
littlesweet = Icecreamstand("littlesweet", ["木瓜", "苦瓜", "idk", "巧克力"])
littlesweet.shop_restaurrant()
littlesweet.show_flavors()
littlesweet.open_res()