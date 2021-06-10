import pymysql

con = pymysql.connect(host="localhost", user="root", password="123456", database="china_back")
cursor = con.cursor()


# 增删改
def update(sql, param):
    cursor.execute(sql, param)
    con.commit()  # 提交到数据库


def select(sql, param, mode="all", size=0):
    cursor.execute(sql, param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)


# 专门关闭连接
def relaseConnect():
    cursor.close()
    con.close()
