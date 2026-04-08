# import random
# print(round(random.random(),2))
# print(random.randrange(1,200))
# # print(len('hello'))
# # print(bool("hello"))


for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print(str(j)+"*"+str(i),end=" ")
    print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for k in range(1,10):
    for l in range(1,10):
        if l>=k:
            print(str(k)+"*"+str(l),end=" ")
    print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")