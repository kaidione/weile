# 打印nxn乘法表
"""def printNxN(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, "x", j, "=", i * j, "\t", end="")
        print()


printNxN(9)
"""

dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
# 1、请循环遍历出所有的key
# print(dict.keys())
for i in dict.keys():
    print(i)
# 2、请循环遍历出所有的value
for i in dict.values():
    print(i)

# 3、请在字典中增加一个键值对,"k4":"v4"
dict["k4"] = "v4"
print(dict)
info = {
    '苹果': 32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
print(info.get("葡萄"))
Fruits = {
    # 水果和单价
    '苹果': 12.3,
    '草莓': 4.5,
    '香蕉': 6.3,
    '葡萄': 5.8,
    '橘子': 6.4,
    '樱桃': 15.8
}
info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': {}
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': {}
    }
}
# 计算每个人花费的金额，并把值传给money
for i in info:
    print(i, "：购物账单")
    if i == "小明":
        for j in info[i]["fruits"]:
            # print(j)
            if j in Fruits.keys():
                a = info[i]["fruits"][j] * Fruits[j]
                a = round(a, 2)
                info[i]["money"][j] = a
        for key in info[i]["money"]:
            print(key, info[i]["money"][key])
        # print(info[i]["money"].values(), info[i]["money"].keys())
    else:
        for j in info[i]["fruits"]:
            # print(j)
            if j in Fruits.keys():
                b = info[i]["fruits"][j] * Fruits[j]
                # print(info[i]["fruits"][j], Fruits[j], b)
                b = round(b, 2)
                info[i]["money"][j] = b
        for key in info[i]["money"]:
            print(key, info[i]["money"][key])
            # print(info[i]["money"].values(), info[i]["money"].keys())


def countNum(li):
    e = {}
    for d in li:
        n = li.count(d)
        e[d] = n
    return e


li1 = [21, 56, 10, 56, 56, 56, 56, 56, 56, 56, 56, 21, 21, 21, 10, 10, 10]
print(countNum(li1))

students = [
    {'name': '张三', 'age': 23, 'score': 88, 'tel': '23423532', 'gender': '男'},
    {'name': '李四', 'age': 26, 'score': 80, 'tel': '12533453', 'gender': '女'},
    {'name': '王五', 'age': 15, 'score': 58, 'tel': '56453453', 'gender': '男'},
    {'name': '赵六', 'age': 16, 'score': 57, 'tel': '86786785', 'gender': '保密'},
    {'name': '小明', 'age': 18, 'score': 98, 'tel': '23434656', 'gender': '女'},
    {'name': '小红', 'age': 23, 'score': 72, 'tel': '67867868', 'gender': '女'},
]
# 1)统计不及格学生的个数

count = 0
for i in students:
    if i["score"] < 60:
        count = count + 1
print(count, "个人不及格")
# 2)b.打印不及格学生的名字和对应的成绩
for i in students:
    if i["score"] < 60:
        print(i["name"], " ", i["score"])
# 3)统计未成年学生的个数
count = 0
for i in students:
    if i["age"] < 18:
        count = count + 1
print(count, "个人未成年")
# 4)打印手机尾号是8的学生的名字
for i in students:
    if i["tel"].isdigit():
        tel = int(i["tel"])
        # print(tel % 10)
        if tel % 10 == 8:
            print(i["name"])
# 5)打印最高分和对应的学生的名字
max1 = 0
for i in students:
    if i["score"] > max1:
        max1 = i["score"]
for i in students:
    if i["score"] == max1:
        print(i["name"])
# 6)将列表按学生成绩从大到小排序
i = 0
s = []
while i < len(students):
    j = i + 1
    while j < len(students):
        if students[j]["score"] > students[i]["score"]:
            s = students[j]
            students[j] = students[i]
            students[i] = s
        j = j + 1
    i = i + 1
print(students)
# max2 = 0
# stu = []
# i = 0
#
# for index, value in enumerate(students):
#     print(students)
#     max2 = value["score"]
#     # print("初始化", max2)
#     j = index + 1
#     while j < len(students[index:]):
#         if max2 < students[j]["score"]:
#             max2 = students[j]["score"]
#
#         j = j + 1
#     print("最大值", max2)
#     for index3, value3 in enumerate(students):
#         if value3["score"] == max2:
#             stu = value
#             students[index] = value3
#             students[index] = stu


# if value2 == max2:
#     stu = students[index]
#     students[index] = students[index2]
#     students[index2] = stu
# a = [1, 2, 3]
# for i in a:
#     print("第一层", i)
#     for j in a:
#         print("第二层", j)

"""stu = []
for index, value in enumerate(students):
    # print(index, value)
    for index1, value1 in enumerate(students[index:]):
        # print(students)
        # print(index1, value1)
        if value["score"] < value1["score"]:
            stu = value
            students[index] = value1
            # print(students[index])
            students[index1+index] = stu
            # print(students[index1])
            print(students)
"""

# 7)删除性别保密的所有学生
for index, value in enumerate(students):
    if value["gender"] == "保密":
        del students[index]
print(students)



