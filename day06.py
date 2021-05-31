import random

print("-------------------超市购物系统----------------------")
# 获取购物车
shoppingCart = []

# 抽取优惠券
coupons = 0
flag = 0
if flag == 0:
    a = input("请问是否立即购物,1表示确认，0表示关闭")
    if a != "":
        flag = a
        coupons = random.randint(1, 9)
        print("恭喜您，获得了", coupons, "折优惠券，可在本次结算时使用")
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
b = input("请输入您的预算金额：")
if b.isdigit():
    budget = int(b)
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
                break
        else:
            print("请输入超市有的商品编号")
elif b == 'Q' or b == 'q':
    print("退出购物成功")
else:
    print("您输入了非法字符，请重新输入")
# print(shoppingCart)
