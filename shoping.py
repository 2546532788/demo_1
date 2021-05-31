#
# -------------------地狗商城系统----------------
#     购物车：
#     1.初始化自己的薪资余额
#     2.展示哪些商品
#     需求：
#         前提：有 3张lenovo的5折券，4张ipnone&mac的6这券。买东西之前随机抽奖。在最终结算的时候使用券完成优惠！
#         1.若金钱够了，可以购买，将当前这个商品添加到购物车。
#         2.若不够，不能购买，温馨提示：穷鬼！金钱不够！
#         3.若商品编号不存在，打印错误信息，给温馨提示：别瞎弄！
#         4.输入Q或者q，购物结束，并打印购物小条。
import random
num_1 = random.randint(1,9)
print("系统抽奖优惠劵：","--------------",num_1)

shop = [
    ["苹果12",9800],
    ["华为p50",6800],
    ["oppen5puls",3400],
    ["vivo8p",2500],
    ["Airpos",1000],
    ["小米手环",300],
]
# 显示商品
for index,value in enumerate(shop):
    print(index,value)

income = input("请输入收入：￥")
income = int(income)
a = 0
b= 0
cat = []    #购物车

while True:
    for index,value in enumerate(shop):
        print(index,"",value)
    num = input("请输入商品编号：")
    if num.isdigit():
        num = int(num)
        if num > len(shop):
            print("该商品没有")
        else:
            if income < shop[num][1]:
                print("您的收入不支持购买商品")
            else:
                cat.append(shop[num])
                income = income - shop[num][1]*num_1*0.1

                print("余额剩下",income)
                # print("购买该商品花了",cat)
                for i,v in enumerate(cat):
                    a = v[1] + a
                print(a*num_1*0.1)
                    # print(i,v)


    elif num =="q" or num == "Q":
        print("欢迎下次光临")
        break
    else:
        print("输入错误，重新输入")
for index,value in enumerate(cat):
    print("已购买商品清单：",index,value)
print("余额剩下：￥",income)


