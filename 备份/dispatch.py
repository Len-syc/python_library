#this is yuanshenlmpaat dispatch by Python 
text_welcomemessage = "welcome to mihoyo dispatch"
text_error = "Error!"
End_message= "mihoyo"
user_SQL = {"test":"10000",}
#account:uid
print(text_welcomemessage)
user_test = "2"
user_account=input("your account:")
user_uid= 10001#input("uid:")
##showuid_SQL = 
#询问用户值
if len(user_account) <4:
    print(text_error)
    print("账号格式有问题，请重新输入")
else:
    print("创立账号中..""\n请稍等""\n完成!")
    print("welcome to mihoyo\n\t",user_account)
    user_SQL[user_account]= user_uid
    ##showuid_SQL["10000"] = user_uid
    print("your account is:",user_account)
    ##print(Uid_SQL)
    print("your uid is:",user_uid)
    print("\naccount:",user_account,"\nuid:",user_uid)
print(End_message)