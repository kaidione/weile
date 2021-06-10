"""from upadate import update, select

sql = "insert into person values(%s,%s,%s)"
param = ["田七", 78, 630.23]

sql1 = "select  * from person"
param1 = []

# 插入操作
update(sql,param)

# 查询操作
data = select(sql1, param1, mode="many", size=3)
print(data)
"""

import random
from operation import update, select

# 银行的库
names = {"1a5sdf1af": {"address": "沙河北大桥桥底下", "money": 546, "userName": "张三", "password": "123456",
                       "country": "中国", "province": "山西", "street": "霍东大道", "door": "301"},
         "1a51af": {"address": "沙河北大桥桥底下", "money": 1006, "userName": "张三", "password": "123",
                    "country": "中国", "province": "山西", "street": "霍东大道", "door": "401"}

         }
'''
{
    "张三":{address:"沙河北大桥桥底下",money:546,account:1a5sdf1af},
    "张三":{address:"沙河北大桥桥底下",money:546}
}
names[account]["country"], names[account]["province"], names[account]["street"],
                      names[account]["door"]
'''
# print(names["1a5sdf1af"].get("password"))
# print(names.values())
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
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "w", "v", "u", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H",
          "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "W", "V", "U", "X", "Y", "Z"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0, len(li) - 1)]
        string = string + ch
    return string


# 银行的开户逻辑
def bank_addUser(account, username, password, money, country, province, street, door):
    # 1.判断是否已满
    sql_add = "select * from china_back"
    param_add = []
    data = select(sql_add, param_add, "all")
    if len(data) >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    # if username in names:
    #     return 2
    # 判断是狗存在该账户
    for i in data:
        if i[0] == account:
            return 2
    # 3.开户
    # names[account] = {
    #     "account": account,
    #     "username": username,
    #     "password": password,
    #     "money": money,
    #     "country": country,
    #     "province": province,
    #     "street": street,
    #     "door": door,
    #     "bank_name": bank_name
    # }
    sql_open = "insert into china_back values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    param_open = [account, username, password, money, country, province, street, door, bank_name]
    update(sql_open, param_open)
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
            门牌号：%s
            开户行名称：%s
            ------------------------------------
        '''
        print(info % (username, password, account, money, country, province, street, door, bank_name))

    elif status == 2:
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")


# 存钱逻辑
def bank_saveMoney(account, password, money):
    # if account in names.keys() and names[account].get("password") == password:
    #     names[account]["money"] = names[account].get("money") + money
    sql_save = "select account,passwords,money from china_back where account = %s and passwords = %s"
    param_save = [account, password]
    data = select(sql_save, param_save, "all")
    if data.__len__() == 1:
        # print(data)
        m = data[0][2] + money
        sql_save1 = "update china_back set money = %s where account = %s"
        param_save1 = [m, account]
        update(sql_save1, param_save1)
        return m
    else:
        return 0


# 存钱操作

def saveMoney():
    account = input("请输入您要存款的账号：")
    password = input("请输入存款账号的密码：")
    money = int(input("请输入您要存的金额："))
    a = bank_saveMoney(account, password, money)
    if a == 0:
        print("账号或密码输入错误")
    else:
        print("存入成功", "您的余额为：", a)


# 取款逻辑
def bank_drawMoney(account, password, money):
    sql_draw = "select account, passwords, money from china_back where account = %s and passwords = %s"
    param_draw = [account, password]
    data = select(sql_draw, param_draw, "all")
    # if account in names.keys():
    #     if password == names[account]["password"]:
    #         if money <= names[account]["money"]:
    #             names[account]["money"] = names[account]["money"] - money
    #         else:
    #             return 3
    #     else:
    #         return 2
    # else:
    #     return 1
    if len(data) == 1:
        if money <= data[0][2]:
            m = data[0][2] - money
            sql_draw1 = "update china_back set money = %s where account = %s"
            param_draw1 = [m, account]
            update(sql_draw1, param_draw1)
            return m
        else:
            return -4
    else:
        return -1


# 取款操作
def drawMoney():
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的取款余额："))
    status = bank_drawMoney(account, password, money)
    if status == -1:
        print("账户不存在或密码错误")
    # elif status == -2:
    #     print("输入密码错误")
    elif status == -4:
        print("余额不足")
    else:
        print("取款成功，剩余余额为", status)


# 银行的转账逻辑
def bank_EFT(account, password, account_1, money):
    # 判断转出和转入账户的是否存在
    if account != account_1:
        sql_eft = "select account, passwords, money from china_back where account = %s and passwords = %s"
        sql_eft1 = "select account, money from china_back where account = %s"
        param_eft = [account, password]
        param_eft1 = [account_1]
        data = select(sql_eft, param_eft, "all")
        data1 = select(sql_eft1, param_eft1, "all")
        if len(data) == 1 and len(data1) == 1:
            if money <= data[0][2]:
                m = data[0][2] - money
                m1 = data1[0][1] + money
                sql_eft2 = "update china_back set money = %s where account = %s"
                sql_eft3 = "update china_back set money = %s where account = %s"
                param_eft2 = [m, account]
                param_eft3 = [m1, account_1]
                update(sql_eft2, param_eft2)
                update(sql_eft3, param_eft3)
                return m
            else:
                return -3
        else:
            return -1
        # if account in names.keys() and account_1 in names.keys():
        #     if password == names[account]["password"]:
        #         if money <= names[account]["money"]:
        #             names[account]["money"] = money + names[account]["money"]
        #             names[account]["money"] = names[account]["money"] - money
        #             return 0
        #         else:
        #             return 3
        #     else:
        #         return 2
        # else:
        #     return 1
    else:
        return -4


# 转账操作
def bank_ert():
    account = input("请输入转出账户:")
    account_1 = input("请输入转入账户:")
    password = input("请输入转出账户的密码：")
    money = int(input("请输入转出的金额:"))
    ll = bank_EFT(account, password, account_1, money)
    if ll == -1:
        print("库中没有转出或转入账户存在或转出密码错误")
    # elif ll == 2:
    #     print("密码错误")
    elif ll == -3:
        print("转出金额本金不足")
    elif ll == -4:
        print("转出账号不能与转入账号一致")
    else:
        print("转账成功，当前账户余额为", ll)


# 查询逻辑
def bank_query(account, password):
    sql_query = "select * from china_back where account = %s and passwords = %s"
    param_query = [account, password]
    data = select(sql_query, param_query, "all")
    if len(data) == 1:
        return 2
    else:
        return 1
    # if account in names.keys():
    #     if names[account]["password"] == password:
    #         return 2
    #     else:
    #         return 3
    # else:
    #     return 1


# 查询操作
def query():
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    status = bank_query(account, password)
    if status == 1:
        print("该账户不存在或密码错误")
    # elif status == 3:
    #     print("密码输入错误")
    elif status == 2:
        sql_query = "select * from china_back where account = %s and passwords = %s"
        param_query = [account, password]
        data = select(sql_query, param_query, "all")
        print("查询结果：")
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
        print(info % (data[0][1], password, account, data[0][3],
                      data[0][4], data[0][5], data[0][6],
                      data[0][7], data[0][8]))


# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        saveMoney()
    elif chose == '3':
        drawMoney()
    elif chose == '4':
        bank_ert()
    elif chose == '5':
        query()
    elif chose == '6':
        print("欢迎下次使用")
        break
    else:
        print("输入非法！别瞎弄！")
