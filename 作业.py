dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
# 1、请循环遍历出所有的key
keys = dict.keys()
# print(keys)
for key in keys:
    print(key, )
# 2、请循环遍历出所有的value
values = dict.values()
# print(values)
for value in values:
    print(value)
# 3、请在字典中增加一个键值对,"k4":"v4"
dict["k4"] = "v4"
print(dict)
# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# 用水果名称做key，金额做value，创建一个字典
# info = {
#     '苹果': 32.8,
#     '香蕉': 22,
#     '葡萄': 15.5
# }
# print(info)
# def info_1(data):
#     for i in data:
#         print(i)
# info_1(info)
# income = input("请输入水果的名称")
# a=info[income]
# print(a)
#
# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，
# 并写入到money字段里。
# 以姓名做key，value仍然是字典
Friuts = {
    "苹果": 12.3,  # 水果和单价
    "草莓": 4.5,
    "香蕉": 6.3,
    "葡萄": 5.8,
    "橘子": 6.4,
    "樱桃": 15.8,
}
info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money':0
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money':0
    }
}

#
# def info_1(data):
#     for i in data:
#         print(i, "\t")
#
#
# money = []
# info_1(Friuts)
# print("小明和小刚的花费金额")
# a = input("请选择水果名称：")
# while True:
#     num = int(input("请输入斤数："))
#     if a in Friuts.keys():
#         num = num * Friuts[a]
#         money.append({a: num})
#         print(num)
#     print(money)
money=[]
for key in info:
    for key1 in info[key]["fruits"]:
        for key2 in Friuts:
            if key1 == key2:
                info[key]["money"] =info[key].get("money")+info[key]["fruits"].get(key1)*Friuts.get(key2)
                # money.append(info)
                # print(money)
print(info)
num = info["小明"]["money"] + info["小刚"]["money"]
print(num)

# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
a = [1,2,3,4,5,6,7,3,4,5,5]
# c = [2,3,43,1]

def b(data):
    b = {}
    for index, value in enumerate(data):
        if value in data[:index]:
            continue
        else:
            # print(value, data.count(value))
            b[value] = data.count(value)
    print(b)
b(a)
# b(c)


# 将中国所有的省会城市添加到字典中。以010:”北京”方式存储。
citys = {
    "010":"北京",
    "020":"上海",
    "030":"广州",
    "040":"深圳"
}
citys["050"] = "石家庄"
print(citys)

# 声明一个列表，在列表中保存6个学生的信息(6个题1中的字典)
students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]



# 1) 统计不及格学生的个数

i = 0
ii = 0
while i < len(students):
    if students[i]["score"] < 60:
        ii = ii +1
        print(students[i]["score"])
    i = i +1
print("不及格的人数为：",ii)
# print(students[5]["score"])
# 2) b.打印不及格学生的名字和对应的成绩
i = 0
while i < len(students):
    if students[i]["score"] < 60:
        print(students[i]["score"],students[i]["name"])
    i = i+1
# 3) 统计未成年学生的个数
i = 0
ii = 0
while i < len(students):
    if students[i]["age"] < 18:
        ii = ii +1
        # print(students[i]["age"])
    i = i +1
print("未成年学生的个数为：",ii)
# 4) 打印手机尾号是8的学生的名字
# print(1234567%10)
i = 0
while i < len(students):
    if int(students[i]["tel"])%10 == 8:
        print(students[i]["tel"],students[i]["name"])

    i = i +1
# 5) 打印最高分和对应的学生的名字
i = 0
num = 0
while i < len(students):
    if students[i]["score"] > num:
        print(students[i]["score"])

    i = i +1
b = sorted(a)
print("最高分为",b[-1])
# 6) 将列表按学生成绩从大到小排序
i = 0
while i < len(students):
    b = i
    while b < len(students):
        if students[i]["score"] < students[b]["score"]:
            c = students[i]
            students[i] = students[b]
            students[b] = c

        b = b + 1
    i = i +1
print(students)
# 7) 删除性别保密的所有学生
i = 0
while i < len(students):
    if students[i]["gender"] == "保密":
        del students[i]

    i = i + 1
print(students)