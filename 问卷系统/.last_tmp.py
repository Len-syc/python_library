print("test")
user_phone = input("请输入你的电话号码:")
test1 = len(user_phone)
test3= user_phone[0]
while test1 < 11 or test1 > 11 or test3 !="1":
    print("号码长度有误，或请输入国内手机号")
    user_phone = input("请重新输入你的电话号码:")
    test1 = len(user_phone)
    test3= user_phone[0]
else:
    print("输入成功")
    print(user_phone)