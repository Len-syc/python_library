class Xudong:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid
        self.src = {"1.0": "1.0.zip", "2.0": "2.0.zip", "3.0": "3.0.zip"}
    def ysleak(self, zip):
        if zip in self.src:
            print(self.src[zip])
lenqing = Xudong("xudong.mhy.com", "100000001" )
leak = lenqing.ysleak("1.0")










