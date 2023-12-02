print("输入后求平均值")
total= 0
count= 0
user_input= input(("请输入数字,Q为结束:"))
while user_input != "q":
    num= float(user_input)
    total = total + num
    count = count + 1
    user_input= input(("请输入数字q为结束:"))
if count == "0":
    f = 0
else:
    f = total / count
print("求得的平均值是",f)