#   打印 1～50 中：能被 3 整除的数（i % 3 == 0）要求所有数字在同一行显示
for i in range(1, 51):
    if i % 3 == 0:
        print(i, end=" ")
print("")
print("~~~~~~~~~~~~")

#   循环下面列表，大于等于 60 输出：及格
#   小于 60 输出：不及格
#   同样用 end= 让结果在一行显示
scores = [55, 78, 92, 43, 68, 81, 39, 100, 59]
for i in scores:
    if (i >= 60):
        print(str(i) + "及格", end=" ")
    if (i < 60):
        print(str(i) + "不及格", end=" ")
print("")
print("~~~~~~~~~~~~")

#   如果数字能被 4 整除，打印：XX是4的倍数
#   否则打印：XX不是4的倍数
#   全部同一行显示
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in nums:
    if(i % 4==0):
        print(str(i)+"是4的倍数",end="")
    else:
        print(str(i)+"不是4的倍数",end="")
print("")
print("~~~~~~~~~~~~")
  # 循环1-10打印
  # for：适合遍历列表、固定次数
  # while：适合先设一个变量，靠条件控制循环
for i in range(1,11):
    while i<11:
        print(i,end=" ")
        i=10+i
print("")
print("~~~~~~~~~~~~")
#   第二种办法循环1-10
i = 1          # 先给一个起始数字
while i <= 10: # 只要 i 小于等于10就继续
    print(i, end=" ")
    i = i + 1  # 每次加1
print("")
print("~~~~~~~~~~~~")

  # 用 while 循环 打印：1~30 中能被 5 整除的数并让它们在同一行显示
i=1
while i <= 30:
    if(i%5 == 0):
        print(i,end=", ")
    i=i+1

print("")
print("~~~~~~~~~~~~")

i = 1
while i <= 30:
    print(i, end=" ")
    if i == 15:
        break  # 到15就直接结束循环
    i = i + 1
print("")
print("~~~~~~~~~~~~")

i = 0
while i < 10:
    i = i + 1
    if i == 5:
        continue  # 跳过5，不打印
    print(i, end=" ")
print("")
print("~~~~~~~~~~~~")
  # 用 while 循环 1~20，遇到 10 就用 break 停下来
i=1
while i<=20:
    if(i==10):
        break
    print(i,end=",")
    i = i + 1
print("")
print("~~~~~~~~~~~~")
  # 用 while 打印 1～10，遇到 5 就跳过不打印，其他数字正常输出。
i=1
while i <10:
    i = i + 1
    if(i == 5 ):
        continue
    else:
        print(i, end=",")
print("")
print("~~~~~~~~~~~~")
