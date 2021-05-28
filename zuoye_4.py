i = 1
while i <= 7:
    j = 1
    while j <= 7-i:
        print(" ",end="")
        j +=1
    k = 1
    while k <= i:
        print('* ', end='')
        k += 1
    print()
    i +=1

#阅读程序并回答问题

"""num = int(input("11"))
while num !=0:
    print(num % 10)
    num = num // 10"""

list = ["北京","上海","重庆"]
list.extend(["太原","武汉","贵阳","南京","呼和浩特","石家庄","深圳","海口"])

print(list)
a = list[1]
list[1]=list[2]
list[2]=a
print(list)

#这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。

gdp = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
"""c = (sum(gdp))
print(c)"""
a = 0
b = 0
c = 0
while c < 8:
    if gdp[a] == gdp[a]:
        b = b +gdp[a]
    a = a + 1
    c = c + 1
print("",b)
#有以下一个列表，求其中是5的倍数的和
q = [1,5,21,30,15,9,30,24]
#sum = ([range(q)%5==0])
#print(sum)
i = 0  #全局变量，总步数
j = 0  #0-7的角标
z = 0  #5的倍数的和
while i < 8:
    if q[j]%5 == 0:
        z = z + q[j]
    j = 1+j
    i = 1 + i
print("总和：",z)

#有下列列表，请编程实现列表的数据翻转
list = [1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)


#请编程统计列表中的每个数字出现的次数
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
print(len(List))
a = 0
b = 0
i = 0
while a < 15:
    i = 0
    b = 0
    while b < 15:
        if a == List[b]:
            i = i + 1
        b = b + 1
    print(a, "出现了", i, "次")
    a = a + 1
