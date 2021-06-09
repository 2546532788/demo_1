import random
import pymysql

db = pymysql.connect(host="localhost", user="root", password="root", database="up")

cursor = db.cursor()


# 增删改
def update(sql, param):
    cursor.execute(sql, param)
    db.commit()  # 提交到数据库


# 查询
def select(sql, param, mode="all", size=0):
    cursor.execute(sql, param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)


# 关闭连接
def relaseConnect():
    cursor.close()
    db.close()


a = []

# db = pymysql.connect(host="localhost",user="root",password="root",database="up")
#
# cursor = db.cursor()
# sql1 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# param = [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]]
# cursor.execute(sql1,param)

# db.commit()
#
# # 5.关闭资源
# cursor.close()
# db.close()
# 银行的库
names = {
    "1a": {"username": "张三", "password": "123456", "money": 900, "country": "中国", "province": "北京", "street": "西安街",
           "door": "12"},
    "a1": {"password": "111111", "money": 10000, },
}
'''
{
    "张三
}
'''

# 开户行名称
bank_name = "中国工商银行昌平支行"
# 欢迎页面的模板
welcome = '''
    -----------------------------------------
    -     欢迎来到中国工商银行账户管理系统     -
    -----------------------------------------
    -   1.开户                               -
    -   2.存钱                               -
    -   3.取钱                               -
    -   4.转账                               -
    -   5.查询                               -
    -   6.Bye!                               -
    ------------------------------------------
'''


def getRandom():
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0, len(li) - 1)]
        string = string + ch
    return string


# 银行的开户逻辑
def bank_addUser(account, username, password, money, country, province, street, door):
    # 1.判断是否已满
    if len(names) >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if username in names:
        return 2
    # 3.开户
    sql = "insert into bank value(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    param = [account, username, password, money, country, province, street, door, bank_name]
    update(sql, param)
    return 1


# 开户操作
def addUser():
    username = input("请输入您的姓名：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的账户余额："))  # "123"  123
    print("下面请输入您的个人地址信息：")
    country = input("请输入您的国籍：")
    province = input("请输入您的省份：")
    street = input("请输入您的居住街道：")
    door = input("请输入您的门牌号：")
    account = getRandom()
    status = bank_addUser(account, username, password, money, country, province, street, door)
    if status == 1:
        print("恭喜开户成功！以下是您的个人信息：")
        info = '''
            ----------个人信息 【工商银行】--------
            用户名：%s,
            密码：%s,
            账号：%s,
            余额：%s,
            国家：%s,
            省份：%s,
            街道:%s,
            门牌号：%s,
            开户行名称：%s,
            ------------------------------------
        '''

        print(info % (username, password, account, money, country, province, street, door, bank_name))
    elif status == 2:
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")


# 存款的逻辑
def bank_DEP(account, money):
    sql1 = "select account,money from bank"
    data = []
    names = select(sql1, data)
    print(names)
    for i in range(0, len(names)):
        if account == names[i][0]:
            money_1 = names[i][1] + money
            sql = "update bank set money=%s where account = %s ;"
            param = [money_1, account]
            update(sql, param)
            return True
    return False


# 存款的操作
def bank_dep():
    account = input("请输入账户：")
    money = int(input("请输入存款金额"))
    aa = bank_DEP(account, money)
    if aa == True:
        print("恭喜成功", money)
    if aa == False:
        print("失败")


# 取款的逻辑
def bank_get(account, password, money):
    sql1 = "select account,password_1,money from bank"
    data = []
    names = select(sql1, data)
    print(names)
    for i in range(0, len(names)):
        print(i)
        if account == names[i][0]:
            if password == names[i][1]:
                if money <= int(names[i][2]):
                    money_2 = names[i][2] - money
                    sql = "update bank set money=%s where account=%s ;"
                    param = [money_2, account]
                    update(sql, param)
                    print(1)
                    break
                else:
                    return 3
            else:
                return 2
        else:
            if i <= len(names) - 1:
                continue
            return 1


# 取款的操作
def bank_GET():
    account = input("请输入账户：")
    password = int(input("请输入密码："))
    money = int(input("请输入取款金额："))
    vv = bank_get(account, password, money)
    if vv == 1:
        print("账户不存在")
    elif vv == 2:
        print("密码错误")
    elif vv == 3:
        print("钱不够")
    else:
        print("取款成功")


# 银行的转账逻辑
def bank_EFT(account, password, account_1, money_1):
    # 判断转出和转入账户的是否存在
    sql1 = "select account,password_1,money from bank"
    data = []
    names = select(sql1, data)
    print(names)
    for i, value in enumerate(names):
        if account_1 == value[0]:
            for ii, values in enumerate(names):
                if account == values[0]:
                    if password == values[1]:
                        if money_1 <= values[2]:
                            money = values[2] - money_1
                            sql = "update bank set money=%s where account=%s;"
                            param = [money, account]
                            update(sql, param)
                            # print(1)
                            money_1 = value[2] + money_1
                            # sql = "update bank set money=%s where account=%s;"
                            param1 = [money_1, account_1]
                            update(sql, param1)
                            return 0
                        return 1
                    return 2
    return 3


# 转账操作
def bank_ert():
    account = input("请输入转出账户")
    account_1 = input("请输入转入账户")
    password = int(input("请输入转出账户的密码："))
    money_1 = int(input("请输入转出的金额"))
    ll = bank_EFT(account, password, account_1, money_1)
    if ll == 1:
        print("库中没有转出和转入账户存在")
    elif ll == 2:
        print("密码错误")
    elif ll == 3:
        print("转出金额本金不足")
    elif ll == 0:
        print("成功")


# 查询账户
def bank_B(account, password):
    sql1 = "select account, username, password_1, money, country, province, street, door, bank_name from bank"
    data = []
    names = select(sql1, data)
    print(names)
    for i, value in enumerate(names):
        if account == value[0]:
            if password == value[2]:
                return 3
            return 2
    return 1


# 查询账户操作：
def bank_b():
    account = input("选择账户：")
    password = int(input("请输入密码："))
    bb = bank_B(account, password)
    if bb == 1:
        print("该用户不存在")
    if bb == 2:
        print("密码错误")
    sql1 = "select account, username, password_1, money, country, province, street, door, bank_name from bank where account=%s"
    data = [account]
    names = select(sql1, data)

    if bb == 3:
        info = '''
                    ----------个人信息 【工商银行】--------
                    用户名：%s,
                    密码：%s,
                    账号：%s,
                    余额：%s,
                    国家：%s,
                    省份：%s,
                    街道:%s,
                    门牌号：%s
                    开户行名称：%s
                    ------------------------------------
                '''
        print(info % (names[0][0], names[0][1], names[0][2], names[0][3],
                      names[0][4], names[0][5], names[0][6],
                      names[0][7], names[0][8]))


# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        bank_dep()
    elif chose == '3':
        bank_GET()
    elif chose == '4':
        bank_ert()
    elif chose == '5':
        bank_b()
    elif chose == '6':

        break
    else:
        print("输入非法！别瞎弄！")



