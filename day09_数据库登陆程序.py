# 导入mysql接口
import pymysql


# 定义检查信息是否输入正确的方法
def check(username, password):
    # 连接数据库
    conn = pymysql.connect(host="localhost", user="root", password="", database="sale")
    # 创建游标
    cursor = conn.cursor()
    sql = "select * from user where username = %s and user_password = %s"
    param = [username, password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    if data.__len__() == 1:
        return 1
    else:
        return 0


# 开始编写登陆程序
while True:
    username1 = input("请输入登陆用户名：")
    password1 = input("请输入登陆用户的密码：")
    flag = check(username1, password1)
    if flag:
        print("登陆成功")
        break
    else:
        print("登陆失败")
