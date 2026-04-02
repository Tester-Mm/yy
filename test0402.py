# 2026.4.2 具体内容如下
# a 数据类型
a=10
b='hello'
c=3.14
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# b 输入，输入的内容默认都是str类型，如果要输入数字，需要转换
name = input("输入你的狗名：")
print(name)

age = int(input("你的年轮是："))
print(type(age))
print(age)

#if简单的判断使用,判断有多个条件用and，拼接的时候要类型一致
core = float(input("输入你的分数："))
if(core>=90):
    #print(str(core)+"成绩优秀！")
    print(f"{core},成绩优秀！")
if(core>=80 and core<90):
    #print(str(core)+"成绩不错！")
    print(f"{core},成绩不错")
if(core>=60 and core<80):
    #print(str(core)+"成绩一般！！")
    print(f"{core},成绩一般")
if(core<60):
    #print(str(core)+"成绩不行！！")
    print(f"{core},成绩不行")

# 第二天综合练习
name = input("你的名字：")
age = int(input("你的年龄："))

print("你好，", name)
print("你今年", age, "岁")

if age >= 18:
    print("你已经成年啦！")
else:
    print("你还是小朋友～")