import random

print("-------------------超市购物系统----------------------")
# 获取购物车
shoppingCart = []

# 抽取优惠券
coupons = 0
flag = 0
# 展示商品列表
goods = [
    ["海绵宝宝玩偶", 200],
    ["三只松鼠", 300],
    ["变形金刚", 400],
    ["瑞士手表", 1000],
    ["茅台", 2000],
    ["电饭煲", 1500]
]
# 定义总消费金额
total = 0
# 预算初始化
budget = 0
# 定义支付金额
money = 0
city = {
    "北京": {
        "昌平": {
            "天通苑": ["海底捞", "呷哺呷哺"],
            "龙泽": ["永辉超市", "永旺超市"]
        },
        "海淀": {
            "公主坟": ["军事博物馆", "中华世纪园"],
            "科普场馆": ["中国科技馆", "北京天文馆"],
            "高校": ["北京大学", "清华大学"]
        },
        "朝阳": {
            "龙城": ["鸟化石国家地质公园", "朝阳南北塔"],
            "双塔": ["朝阳凌河公园", "朝阳凤凰山"]
        }
    },
    "上海": {}
}


# 打印城市函数
def print_city(data):
    for i in data:
        print(i, "\t")


print_city(city)
chose1 = input("请输入城市:chose1>>>")

while True:
    if chose1 in city:
        print_city(city[chose1])
        chose2 = input("请输入二号景区chose2>>>：")
        if chose2 in city[chose1]:
            print_city(city[chose1][chose2])
            chose3 = input("请输入三号景区chose3:>>>>")
            if chose3 in city[chose1][chose2]:
                print_city(city[chose1][chose2][chose3])
                x = input("是不是选择买点东西,1是,0不是:")
                while x:

                    b = input("请输入您的预算金额：")
                    print(b)
                    if b.isdigit():
                        budget = int(b)
                        # print(budget)
                        if flag == 0:
                            a = input("请问是否立即购物,1表示确认，0表示关闭")
                            if a != "":
                                flag = a
                                coupons = random.randint(1, 9)
                                print("恭喜您，获得了", coupons, "折优惠券，可在本次结算时使用")
                        # 开始购物
                        while flag:
                            for index, value in enumerate(goods):
                                print(index, " ", value)
                            h = input("请输入您要选购的编号：")
                            if h.isdigit():
                                num = int(h)
                                if 0 <= num < len(goods):
                                    if budget >= goods[num][1]:
                                        shoppingCart.append(goods[num])
                                        budget = budget - goods[num][1]
                                        print("此次加购物车所剩预算金额：", budget)
                                    else:
                                        print("购买该商品将会超出预算")
                            # 打印购物小票
                            elif h == 'Q' or h == 'q':
                                if shoppingCart.__len__() != 0:
                                    for index, value in enumerate(shoppingCart):
                                        print(index, " ", value)
                                        total = int(value[1]) + total
                                    money = input("请支付金额：")
                                    print("总计消费：", total * coupons * 0.1)
                                    print("剩余金额：", int(money) - total * coupons * 0.1)
                                    flag = 0
                                    break
                            else:
                                print("请输入超市有的商品编号")
                    elif b == 'Q' or b == 'q':
                        print("退出购物成功")
                        x = 0
                        break
                    else:
                        print("您输入了非法字符，请重新输入")
                        x = 0
                        break
            elif chose3 == 'q' or chose3 == 'Q':
                print("欢迎下次光临！")
                break
