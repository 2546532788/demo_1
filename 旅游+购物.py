while True:
    print("1旅游","2购物")
    a=input("请选择业务")
    if a == "1":
        city = {
            "甘肃":{

            },
            "山西":{
                "太原":{
                    "景点":["柳巷","晋祠","山西博物馆"],
                    "美食":{"灌肠":23,"过油肉":64,"羊杂割":34},
                },

                "大同":{
                    "景点":["云冈石窟","城墙","方特"],
                    "美食":{"刀削面":12,"兔头":45,"杏脯":23},
                },
            },
            "河北":{
                "张家口":{
                    "景点":["塞上草原"],
                    "美食":{"烤羊排":300}
                },
                "承德":{
                    "景点":["避暑山庄"],
                    "美食":{"风干鸡":20}
                }
            }
        }
    # print(city)
        print("==================欢迎来到景点查询？？？特产购物平台台===================")
        def city_1(data):
            for i in data:
                print(i,"\t")

        city_1(city)
        chose_1 = input("请输入省份：")

        while True:
            if chose_1 in city:
                city_1(city[chose_1])
                chose_2 = input("请输入城区：")
                if chose_2 in city[chose_1]:
                    city_1(city[chose_1][chose_2])
                    chose_3 = input("请选择美食或者是景点：")
                    if chose_3 in city[chose_1][chose_2]:
                        city_1(city[chose_1][chose_2][chose_3])
                        break
                    elif chose_3 == "q" or chose_3 == "Q":
                        print("欢迎下次光临")
                        break
            elif chose_1 == "q" or chose_1 == "Q":
                print("欢迎下次光临")
                break
            break
    if a == "2":
        import random

        a = input("随意输入任何数字领取优惠劵：")
        a = int(a)
        num_1 = random.randint(1, 9)
        print("系统抽奖优惠劵：", "--------------", num_1)

        shop = [
            ["苹果12", 9800],
            ["华为p50", 6800],
            ["oppen5puls", 3400],
            ["vivo8p", 2500],
            ["Airpos", 1000],
            ["小米手环", 300],
        ]
        # 显示商品
        for index, value in enumerate(shop):
            print(index, value)

        income = input("请输入收入：￥")
        income = int(income)
        a = 0
        b = 0
        cat = []  # 购物车

        while True:
            for index, value in enumerate(shop):
                print(index, "", value)
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
                        income = income - shop[num][1] * num_1 * 0.1

                        print("余额剩下", income)
                        # print("购买该商品花了",cat)
                        for i, v in enumerate(cat):
                            a = v[1] + a
                        print(a * num_1 * 0.1)
                        # print(i,v)


            elif num == "q" or num == "Q":
                print("欢迎下次光临")
                break
            else:
                print("输入错误，重新输入")
        for index, value in enumerate(cat):
            print("已购买商品清单：", index, value)
        print("余额剩下：￥", income)
    else:
        print("退出系统，欢迎下次光临")
        break
    break



