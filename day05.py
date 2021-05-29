chinese = ['小明', '小张', '小黄', '小杨']
math = ['小黄', '小李', '小王', '小杨', '小周']
english = ['小杨', '小张', '小吴', '小冯', '小周']
a = []
print(a)
# 求选课学生总共有多少人
print("求选课学生总共有多少人")
for data in chinese:
    if data not in a:
        a.append(data)
for data in math:
    if data not in a:
        a.append(data)
for data in english:
    if data not in a:
        a.append(data)
print("选课的学生共有：", len(a))
# print(num1)
# 求只选了第一个学科的人的数量和对应的名字
print("只选了第一个学科的人的数量和对应的名字")
for data in chinese:
    print("选第一个学科的人的名字：", data)

print("选第一个学科的数量：", len(chinese))

# 求只选了一门学科的学生的数量和对应的名字
print("求只选了一门学科的学生的数量和对应的名字")
person = []

for data in chinese:
    person.append(data)
for data in math:
    person.append(data)
for data in english:
    person.append(data)
i = 0
count1 = 0
while True:
    if i == person.__len__():
        break
    if person.count(person[i]) == 1:
        count1 = count1 + 1
        print("只选择了一个学科的姓名：", person[i])
    i = i + 1
print("只选择了一个学科的人数：", count1)

# 求只选了语文和英语的学生的数量和对应的名字
print("只选了语文和英语的学生的数量和对应的名字")
j = 0
count2 = 0
while True:
    if j == person.__len__():
        break
    if person.count(person[j]) == 2 and person[j] not in math:
        if person[j] not in person[:j]:
            count2 = count2 + 1
            print("只选了语文和英语的学生：", person[j])
    j = j + 1
print("只选了语文和英语的学生的人数：", count2)

"""i = 9
while i > 0:
    j = 1
    while j <= i:
        print(i, "x", j, "=", i*j, end="  ")
        j = j + 1
    print()
    i = i - 1
"""

"""
# 排序
i = 0
li = []
while i < 5:
    print("请输入第", i + 1, "个数：")
    a = input()
    li.append(a)
    i = i + 1
print(li)

# li = [1, 2, 3, 5, 3]
# print(li[:2])
b = 0
a = 0
while b < li.__len__():
    j = b + 1
    while j < li.__len__():
        if li[b] > li[j]:
            a = li[b]
            li[b] = li[j]
            li[j] = a
        j = j + 1
    b = b + 1

print(li)

"""
