class BankAccount:
    def __init__(self, account_number, balance):
        self.account = account_number
        self.balance = balance
        self.amount = {"all_money": 0, "get_money": 0, "back_money": 0}

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("你存了:", deposit_amount, "你剩余的钱是:", self.balance)

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount <= self.balance:  # 添加判断条件，确保取款金额不超过余额
            self.balance -= withdrawal_amount
            print("你取了:", withdrawal_amount, "你剩余的钱是:", self.balance)
        else:
            print("你的余额不足，无法完成取款")

    def get_balance(self):
        print(f"账号{self.account} (剩余钱：{self.balance})")

    def __str__(self):
        return f"你的账号是: {self.account}, 你的剩余的钱是: {self.balance}"


lenqing = BankAccount("12345678", 100)
xudong = BankAccount("54321", 200)

print("欢迎来到bank")
#print(f"lenqing, 你账户的余额是: {lenqing.balance}")
#print(f"xudong, 你账户的余额是: {xudong.balance}")

token = input("请登入你的账号:")
while token != "12345678" and token != "54321":  # 修正判断条件
    print("输入有误")
    token = input("你的账号:")
else:
    print("正在登入中")
    name = token
    if name == "12345678":
        account = lenqing
    else:
        account = xudong
    print(f"欢迎来到bank")
    print(f"{name}, 你账户的余额是: {account.balance}")

token2 = input("请问你要存钱还是取钱:(输入'q'退出)")
while token2 != "q":
    if token2 == "存钱":  # 修正判断条件
        amount = input("请问存多少RMB:")
        account.deposit(int(amount))
    elif token2 == "取钱":  # 修正判断条件
        amount = input("请问取多少RMB:")
        account.withdraw(int(amount))
    else:
        print("输入有误")

    token2 = input("请问你要存钱还是取钱:(输入'q'退出)")
