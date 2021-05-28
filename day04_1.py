"""# 打印等边三角形
i = 1
while i <= 7:
    j = 1
    k = 1
    while j <= (7 - i):
        print(" ", end="")
        j = j + 1
    while k <= i:
        print("* ", end="")
        k = k + 1
    print()
    i = i + 1
"""


"""num = int(input("请输入一个数："))
while num != 0:
    print(num % 10)
    num = num // 10"""

"""a = ["北京", "上海", "广东"]
c = ["太原", "天津", "西安", "海南", "包头"]
index = 0
while index < c.__len__():
    a.append(c[index])
    index = index + 1
print(a)

a[1] = "广东"
a[2] = "上海"
print(a)"""

"""d = [36710.36, 35427.10, 29863.23, 29667.39, 27665.36, 27650.45, 27620.38, 25369.20]
i = 0
sum1 = 0
while i < d.__len__():
    sum1 = sum1 + d[i]
    i = i + 1
print(sum1)

print(sum1/d.__len__())"""

"""e = [1, 5, 21, 30, 15, 9, 30, 24]
i = e.__len__()
j = 0
sum2 = 0
while j < i:
    if e[j] % 5 == 0:
        sum2 = sum2 + e[j]
    j = j + 1
print("5的倍数的和：", sum2)
"""

"""list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list.reverse()
print(list)"""


list = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
a = 0
i = 0
num1 = []
num2 = []
while i < list.__len__():
    count = 0
    j = 0
    while j < list.__len__():
        if list[i] == list[j]:
            count = count + 1
        j = j + 1
    if list[i] not in num1:
        num1.append(list[i])
        num2.append(count)
    i = i + 1
while a < num1.__len__():
    print(num1[a], "出现次数", num2[a])
    a = a + 1




