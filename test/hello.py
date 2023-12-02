print('test')
class Cutacat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
    def speak(self):
        print('瞄'  * self.age)
    def think(self,content):
        print(f'小猫{self.name}在思考{content}....')

cat1 = Cutacat('lenqing',1,'blue')
cat1.think('现在是几点')