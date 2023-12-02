text_tittle= "welcome to test Python"
text_service= "this is test\nCB1\n\tby lenqing\nat 5.21"
index_password= input("password:")
text_error="Error!"
text_MiHoYo = "welcome to mihoyo server"
#变量
print(text_tittle)
print(text_service)
print(len(index_password))
print("\nhello\nworld","\nhello\nPython")
#进入标语
if int(len(index_password)) >9:
    print(text_error)
if index_password =="MiHoYo2012":
    print(text_MiHoYo)
else:
    print("welcome\nxudong@mihoyo.com")
    print(text_error,"\n请重新输入")
if index_password =="MiHoYo2012":
    ##text_user=1
##else:
    text_user = str(input("return your Permissions："))
if text_user== "1":
    print("admin")
elif text_user == "2":
    print("root")
elif text_user == "3":
    print("work")
elif text_user =="4":
    print("user")
elif text_user <"0":
    print(text_error)
else:
    print("no user")