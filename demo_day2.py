#运动衫
number_1 = "001"
name_1 = "运动衫"
price_1 = 300
num_1 = 200
kind_1 = "上衣"
stock_1 = "广东"
#T恤
number_2 = "002"
name_2 = "T恤"
price_2 = 300
num_2 = 200
kind_2 = "上衣"
stock_2 = "广东"
#西装裤
number_3 = "003"
name_3 = "西装裤"
price_3 = 100
num_3 = 200
kind_3 = "裤子"
stock_3 = "广东"
#休闲裤
number_4 = "003"
name_4 = "休闲裤"
price_4 = 300
num_4 = 330
kind_4 = "裤子"
stock_4 = "广东"
#羽绒服
number_5 = "005"
name_5 = "羽绒服 "
price_5 = 300
num_5 = 200
kind_5 = "外套"
stock_5 = "广东"
#小西装
number_6 = "006"
name_6 = "小西装"
price_6 = 300
num_6 = 20
kind_6 = "外套"
stock_6 = "广东"

print("=======================欢迎来到衣服购物商场===========================")
print("编号         名称          价格         数量         种类        进货地")
print("------------------------------------------------------")
print(number_1,"       ",name_1,"       ",price_1,"        ",num_1,"       ",kind_1,"       ",stock_1," ")
print(number_2,"       ",name_2,"         ",price_2,"          ",num_2,"       ",kind_2,"       ",stock_2," ")
print(number_3,"       ",name_3,"       ",price_3,"        ",num_3,"       ",kind_3,"       ",stock_3," ")
print(number_4,"       ",name_4,"       ",price_4,"        ",num_4,"       ",kind_4,"       ",stock_4," ")
print(number_5,"       ",name_5,"       ",price_5,"        ",num_5,"       ",kind_5,"       ",stock_5," ")
print(number_6,"       ",name_6,"       ",price_6,"        ",num_6,"       ",kind_6,"       ",stock_6," ")

print("----------------------------")
print("总金额为：￥",(price_1 * num_1 + price_2 * num_2 + price_3 * num_3 + price_4 * num_4 + price_5 * num_5 + price_6 * num_6  ))
#print("总金额为：￥",(price_1 * num_1))
input("name=")