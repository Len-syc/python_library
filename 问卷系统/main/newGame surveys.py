#t问卷
test_message = "hello tester"
test_error = "Error"
verify1 =("False")
verify2= ("False")
verify3 = ("False")
verify4=("False")
verify5=("0")
print(test_message)
database_SQL= {"account":"tester","uid":"10000","key":"GenShinDev-userkey-","ClientURL":"null"}
print("\n\t原神beta问卷调查","\n\thttps://ys.mihoyo.com")
print("\n\t1=yes","\n\t2=no")
answer1 = input("是否有意参加beta测试：")
print("-----------------MiHoYo-----------------")
if answer1 == "1":
    verify5 = input("您的游戏等级为:")
    if "50"<verify5<"61":
        print(" ")
    else:
        print("您的条件不足","无法进行以下的问答")
elif answer1 == "2":
    print("感谢您参加本次测试")
else:
    print("输入有误")
if "50"<verify5<"61":
    age = input("你的年龄是:")
    if age < "18":
        print("你的年龄未成年.感谢你参加本次问卷")
        y = "false"
    else:
         verify2= "True"
else:
    print(test_error)
if verify2 == "True":
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
        verify3="True"
        print(verify3)
else:
    print(test_error)
if verify3 == "True":
    print("""《米哈游保密协议》测试保密协议，如果你在测试过程中，泄露游戏的相关内容，我们将会依法追查""")
    verify4= input("是否同意？""\n同意为y，不同意为n:")
else:
    print(test_error)
if verify4 =="n":
    print("感谢您参加本次问卷")
else:
    print("-----------------MiHoYo-----------------")
if verify4 =="y":
    user_relaccount = input("请输入你的账号:")
    if len(user_relaccount)<12:
        print("输入完成")
        answer2 =("True")
        print(answer2)    
    else:
        print("账号格式错误.最后1次输入机会")
        print("账号格式有误请重新输入")
        user_relaccount = input("请重新输入你的账号:")
else:
    print(test_error)
token1= str(user_phone)
print("正在发送测试账号")
#######
token = str(("GenShinDev-userkey-"))
token2 = str(("-value=GenShinImpactdevkitClient20220524"))
token3 = str((user_relaccount))
token4 = ("-accountkey-")
database_SQL["account"] = user_relaccount
phone_uid = user_phone[3]
databaseuid = database_SQL["uid"]
testuid = databaseuid + phone_uid
test_password= str(user_relaccount) + str(testuid)
##print(test_password)
test_key = token + str(user_phone) + token4 + token3 + token2
database_SQL["key"] = test_key
database_SQL["ClientURL"] = "https://autopatchhk.yuanshen.com/client_app/destincy.zip"
###print(test_key)
######
print("-----------------MiHoYo-----------------")
print("你的测试账号:",user_relaccount)
print("你的测试uid:",testuid)
print("你的测试密码:",test_password)
print("你的key",database_SQL["key"])
print("Client:",database_SQL["ClientURL"] )
print("\n\t原神beta","\n\thttps://ys.mihoyo.com")
