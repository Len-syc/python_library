#题目三：
#编写一个名为 "BankAccount" 的类，具有以下特征：
#构造函数接受两个参数：account_number（账号）和 balance（余额），并将它们分别赋给对象的属性。
#定义一个方法 deposit，接受一个参数 amount（存款金额），并将该金额加到余额上。
#定义一个方法 withdraw，接受一个参数 amount（取款金额），并从余额中减去该金额。
#定义一个方法 get_balance，用于返回当前余额。
#"BankAccount" 的类，它具有以下特征和方法：
#构造函数：构造函数应接受两个参数 account_number（账号）和 balance（余额）
#在构造函数中，将这两个参数分别赋值给对象的属性，以便在后续的方法中使用。
#存款方法 deposit：该方法应接受一个参数 amount（存款金额），
#并将该金额加到账户的余额上。存款后，余额应更新为新的值。
class BankAccount:
    def __init__(self,account_number, blance):
        self.account = account_number
        self.blance = blance
        self.amount = {"all_money":0,"get_money":0,"back_money":0}
    def  deposit(self,get):
        all_money = self.blance
        get_money = get
        finaly_money = all_money - get_money
        print("你取了:",get_money,"你剩余的钱是:",finaly_money )
    def withdraw(self,back):
        all_money = self.blance + back
    def get_balance(self,now_money):
        print(f"账号{self.account} (剩余钱：{self.blance}) ")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")

    def __str__(self):
        return f"account: {self.account}, money: {self.blance}"
lenqing = BankAccount("123456","10000")
lenqing.deposit(100)







#答案
