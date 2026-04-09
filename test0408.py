# 循环列表
names = ["张三", "李四", "王五"]

for name in names:
    print(name)

# 循环指定次数 range(次数)
for i in range(5):
    print("循环第", i, "次")

# while （条件满足会一直跑）
i=0
while i<5:
    print(i)
    i = i + 1   # 持续循环，直到条件不满足才跳出

for i in range(10):
    if i == 3:
        continue  # 跳过3，所以continue的时候是回到for循环，而不是继续下一步的意思
    if i == 6:
        break     # 到6就停 所以break的时候其实是直接退出循环
    print(i)

# 列表循环
user_list = [{"name": "a"}, {"name": "b"}]
for user in user_list:
    print(user["name"])
#用 while 循环打印：1 2 3 4 5 6 7 8 9 10
i=0
while i<11:
    print(i)
    i=i+1

# 用 for 循环打印 0~9 的数字，并在 PyCharm 中打断点，观察每次循环里 i 的值
for i in range (0,10):
    print(i);
    i = i+1;

# 使用 for 循环把每一个名字打印出来
names = ["小明", "小红", "小刚", "小李"]
for user in names:
    print(user)

# 使用 for 循环，按下面格式打印每个人的信息：姓名：xxx，年龄：xx
user_list = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 20},
    {"name": "王五", "age": 22}
]
for user in user_list:
    print("姓名："+user["name"]+",年龄："+str(user["age"]))

# 打印出1-100之间的偶数和奇数
for i in range (1,101):
    if 2 != 1:
        print("偶数是:" +str(i))
    else:
        print("奇数是:"+str(i))

# 使用 for 循环，只打印出 大于 60 的成绩
scores = [55, 78, 92, 43, 68, 81, 39]
for percent in scores:
    if (percent >= 60):
        print(percent)