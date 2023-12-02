class Account:
    def __init__(self, account, poss, uid):
        self.account = account
        self.poss = poss
        self.uid = uid
        self.data = {"account": "test", "poss": 123, "uid": 1001}

    def get_player(self):
        if self.account in self.data:
            self.data["account"] = self.account
        if self.poss in self.data:
            self.data["poss"] = self.poss
        if self.uid in self.data:
            self.data["uid"] = self.uid

    def __str__(self):
        return f"Account: {self.account}, Poss: {self.poss}, UID: {self.uid}"


lenqing = Account("lenqing", "mihoyo2012", "100001")
lenqing.get_player()
print(lenqing)
