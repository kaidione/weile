import random
print("=====================================猜数游戏======================================")

num = int(random.randint(1, 100))
count = 0
money = 5000
print("             -----------------------------------------------------------")

while money - 100 >= 0:
    if count >= 7:
        break
    count = count + 1
    guess = int(input("                             请输入要猜的数字："))
    print("             -----------------------------------------------------------")
    if guess > num:
        money = money - 100
        print("                             提示：大了,余额：", money, "次数：", count)
        print("             -----------------------------------------------------------")
    elif guess < num:
        money = money - 100
        print("                             提示：小了,余额：", money, "次数：", count)
        print("             -----------------------------------------------------------")
    else:
        money = money - 100
        if count <= 3:
            money = money + 200
        else:
            money = money + 150
        print("                             恭喜您!猜对了，一共猜了", count, "次", "余额还有", money)
        print("             -----------------------------------------------------------")
        break
if count == 7:
    print("                             猜错7次已锁定")
if money == 0 or money < 1000:
    print("                             很遗憾！金币已用完，请充值再战")
    print("             -----------------------------------------------------------")




"""
i = 10
sum1 = 0
while i > 0:
    i = i - 1
    a = int(input("请输入一个数字："))
    sum1 = a + sum1
print("输入10个数字的和：", sum1)
"""

"""
i = 10
sum2 = 0
avg = 0
b = 0
c = 0
while i > 0:
    i = i - 1
    a = int(input("请输入一个数字"))
    sum2 = sum2 + a
    avg = sum2 / 10
    if a > b:
        b = a
    else:
        c = a
print("最大的数:", b, "10个数的和:", sum2, "平均数:", avg)
"""

"""
import random

d = int(random.randint(50, 150))
print("产生50——150之间的数:", d)
"""

"""
i = 2
a = 0
b = 0
c = 0
count = 0
while i >= 0:
    count = count + 1
    d = int(input("请输入三角形的一边:"))
    if count == 1:
        a = d
    elif count == 2:
        b = d
    elif count == 3:
        c = d
        break
while a + b > c and a + c > b:
    if a == b == c:
        print("该三角形是等边三角形,三边分别是：", a, b, c)
    elif a == b or a == c or b == c:
        print("该三角形是等腰三角形,三边分别是：", a, b, c)
    elif a ^ 2 + b ^ 2 == c ^ 2 or a ^ 2 + c ^ 2 == b ^ 2 or b ^ 2 + c ^ 2 == a ^ 2:
        print("该三角形是直角三角形,三边分别是：", a, b, c)
    else:
        print("该三角形是普通三角形,三边分别是：", a, b, c)
    break
if a + b <= c or a + c <= b or b + c <= a:
    print("不能组成三角形")

A = 56
B = 78

C = A + B - A
B = A + B - B
A = C
print(A, B)
"""


"""name = "root"
password = "admin"
i = 3
while i > 0:
    i = i - 1
    a = input("请输入密码")
    if a == password:
        print("登陆成功")
        break
    elif a != password:
        print("密码错误")
if i == 0:
    print("密码输错3次，已锁定")
"""

"""sum5 = 0
while True:
    i = int(input("请输入一个1-100之间的数"))
    if 1 <= i <= 100:
        sum5 = sum5 + i
        print("当前累计的和", sum5)
    else:
        print("输入的超出范围，请重新输入")
"""

"""
a = 0
b = 20
d = 0
while True:
    if a < b - 3:
        a = a + 3 - 2
    else:
        d = d + 1
        break
    d = d + 1
print("青蛙第", d, "天能出来")

"""


