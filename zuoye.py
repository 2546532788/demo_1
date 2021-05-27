import random
#实现输入10个数字，并打印10个数的求和结果
a = 1
while a <= 10:
    print(a)
    a =a + 1
print(sum(range(1,10)))

#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
a = (12,23,43,32,56,78,13,11,90,29)
b = sorted(a)
print(b[-1])
c = (sum(a)+(10))
print(c)
d = (sum(a)/(10))
print(d)

#使用random模块，如何产生 50~150之间的数？
a = 50
while a <=150:
    print(a)
    a = a + 1
#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
a = int(input("请输入第一条边长："))
b = int(input("请输入第二条边长："))
c = int(input("请输入第三条边长："))

while True:
    if a == b == c :
        print("是等边三角形")
    elif (a==b or b==c or a==c):
        print("是等腰三角形")
    elif (a*a+b*b==c*c or a*a+b*b==c*c or a*a+b*b==c*c ):
        print("是直角三角形")
    elif (a+b==c or a + c ==b or b + c == a):
        print("普通三角形")
    else:
        print("不能构成三角形")

    break
#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
time = 0
while True:
    name = "root"
    password = "admin"
    time = time + 1
    b = input("请输入用户名：")
    a=input("请输入密码：")
    if password == a:
            print("密码正确，登录成功")
            break
    if password != a:
            print("密码错误")
    elif name != b:
            print("用户名错误")
            break
    if time >= 3:
        print("三次输入错误，自动关闭")
        break
#使用while编程实现求1~100以内的数的和！
a = 1
while a <= 100:
    print(a)
    a = a + 1

print(sum(range(1,100)))

