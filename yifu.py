#将《12月衣服的销售数据》使用变量的方式存储，并进行计算每件衣服的销售占比，
#每种衣服的在本月的销售额占比，本月总销售额。并最终打印到控制台上。
print("=========欢迎来到cc服装店=========")
date = ["1号","2号","3号","4号","5号","6号","7号"]
name = ["羽绒服","牛仔裤","风衣","皮草","T恤","衬衫","牛仔裤"]
price = [253.6,86.3,96.8,135.9,65.8,49.3,86.3]
quantity = [500,600,335,855,632,562,600]
sells_number = [10,60,43,63,63,120,72]
print("日期","服装名称","价格/件","库存数量","销售量/每日")
print(date[0],name[0],price[0],quantity[0],sells_number[0])
print(date[1],name[1],price[1],quantity[1],sells_number[1])
print(date[2],name[2],price[2],quantity[2],sells_number[2])
print(date[3],name[3],price[3],quantity[3],sells_number[3])
print(date[4],name[4],price[4],quantity[4],sells_number[4])
print(date[5],name[5],price[5],quantity[5],sells_number[5])
print(date[6],name[6],price[6],quantity[6],sells_number[6])
print("===================显示==========================")
a = (price[0] * sells_number[0] + price[1] * sells_number[1]+price[2] * sells_number[2] + price[3] * sells_number[3]+price[4] * sells_number[4]+price[5] * sells_number[5]+price[6] * sells_number[6])
print("销售总金额：￥",a)

b = (sells_number[0]+sells_number[1]+sells_number[2]+sells_number[3]+sells_number[4]+sells_number[5]+sells_number[6])
print("销售总数量：",b)

c = (price[0] * sells_number[0])
print("羽绒服销售总金额：￥",c)

print("羽绒服销售占比：￥",round(sells_number[0]/b*100,2),"%")

print("羽绒服销售额占比：￥",round(c/a*100,2),"%")




a = 56
b = 78
print("a=",(a+b-a))
print("b=",(a+b-b))


print("hello world")
a = 6++9
print(a)
stu1 = 45
stu2 = 23
b = stu1 + stu2
print(b)
num1 = 23
num2 = 45
num3 = 56
print(num1+num2+num3)
num1 = 45
num2 = num1
print(num2)
chromeDriver = "谷歌驱动"
gekodriver = "火狐驱动"