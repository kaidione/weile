import random

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
# print(names["1a5sdf1af"].get("money"))
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
    if len(names) >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if username in names:
        return 2
    # 3.开户
    names[account] = {
        "account": account,
        "username": username,
        "password": password,
        "money": money,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "bank_name": bank_name
    }
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
    if account in names.keys() and names[account].get("password") == password:
        names[account]["money"] = names[account].get("money") + money
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
        print("存入成功", "您的余额为：", names[account].get("money"))


# 取款逻辑
def bank_drawMoney(account, password, money):
    if account in names.keys():
        if password == names[account]["password"]:
            if money <= names[account]["money"]:
                names[account]["money"] = names[account]["money"] - money
            else:
                return 3
        else:
            return 2
    else:
        return 1


# 取款操作
def drawMoney():
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的取款余额："))
    status = bank_drawMoney(account, password, money)
    if status == 1:
        print("账户不存在")
    elif status == 2:
        print("输入密码错误")
    elif status == 3:
        print("余额不足")
    else:
        print("取款成功，剩余余额为", names[account]["money"])


# 银行的转账逻辑
def bank_EFT(account, password, account_1, money_1):
    # 判断转出和转入账户的是否存在
    if account in names.keys() and account_1 in names.keys():
        if password == names[account]["password"]:
            if money_1 <= names[account]["money"]:
                names[account_1]["money"] = money_1 + names[account_1]["money"]
                names[account]["money"] = names[account]["money"] - money_1
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


# 转账操作
def bank_ert():
    account = input("请输入转出账户:")
    account_1 = input("请输入转入账户:")
    password = input("请输入转出账户的密码：")
    money_1 = int(input("请输入转出的金额:"))
    ll = bank_EFT(account, password, account_1, money_1)
    if ll == 1:
        print("库中没有转出或转入账户存在")
    elif ll == 2:
        print("密码错误")
    elif ll == 3:
        print("转出金额本金不足")
    elif ll == 0:
        print("转账成功，当前账户余额为", names[account]["money"])


# 查询逻辑
def bank_query(account, password):
    if account in names.keys():
        if names[account]["password"] == password:
            return 2
        else:
            return 3
    else:
        return 1


# 查询操作
def query():
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    status = bank_query(account, password)
    if status == 1:
        print("该账户不存在")
    elif status == 3:
        print("密码输入错误")
    elif status == 2:
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
        print(info % (names[account]["userName"], names[account]["password"], account, names[account]["money"],
                      names[account]["country"], names[account]["province"], names[account]["street"],
                      names[account]["door"], bank_name))


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
