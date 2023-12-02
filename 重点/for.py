for x in "banana":
  print(x)
#打印每一个字母
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#打印列表的item
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break#如果x等于香蕉的自动退出
#会显示出苹果香蕉
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#只会显示苹果,香蕉不会显示
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#不输出banana
for x in range(10):
  print(x)
#如需循环一组代码指定的次数，我们可以使用 range() 函数，range() 函数返回一个数字序列，默认情况下从 0 开始，并递增 #1（默认地），并以指定的数字结束。


