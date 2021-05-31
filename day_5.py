# 排序
a = [1,2,4,3]
i = 0
# print(len(a))
while i < len(a):
    b = i
    while b < len(a):
        if a[i] > a[b]:
            c = a[i]
            a[i] = a[b]
            a[b] = c
        b = b + 1
    i = i +1
print(a)

aa = ['小明','小张','小黄','小杨']
bb = ['小黄','小李','小王','小杨','小周']
cc = ['小杨','小张','小吴','小冯','小周']

# 1) 求选课学生总共有多少人
dd = aa + bb + cc
print(dd)
num = []
for data in dd:
    if data not in num:
        num.append(data)
print(len(num))
# 2) 求只选了第一个学科的人的数量和对应的名字
i = 0
while i < len(aa):
    print(i+1,aa[i])
    i = i +1
# 3) 求只选了一门学科的学生的数量和对应的名字
dd = ['小明', '小张', '小黄', '小杨', '小黄', '小李', '小王', '小杨', '小周', '小杨', '小张', '小吴', '小冯', '小周']
i = 0
ii = 0
while i < len(aa):
    if dd.count(dd[i]) == 1:
            ii = i +1
            print(dd[i])
    if i == len(dd):
            break
    i = i +1
print(ii)
# 4) 求只选了语文和英语的学生的数量和对应的名字
#
qq = 0
w = 0
while qq < len(dd):
    if qq == len(dd):
        break
    if dd.count(dd[qq]) == 2 and dd[qq] not in bb:
        w = w +1
        print(dd[qq])

    i = i + 1
print(w)

# print(dd)
# i = 0
# count1=0
# while True:
#     if i == len(dd):
#         break
#     if dd.count(dd[i]) == 2 and dd[i] not in bb:
#         count1 = count1 +1
#         print("名字",dd[i])
#     i = i +1
# print("数量",count1)



# 99乘法表
i = 9
while i >= 1:
    a = 1
    while a <= i:
        print(i,"X",a,"=",(i*a)," ",end="")
        a = a+1
    print()
    i = i - 1