id1 = '01'
idName1 = "羽绒服"
brand1 = "A"
price1 = 100
discount1 = 7
story1 = 120
size1 = "均码"

id2 = '02'
idName2 = "T恤衫"
brand2 = "B"
price2 = 110
discount2 = 8
story2 = 110
size2 = "均码"

id3 = '03'
idName3 = "风衣"
brand3 = "C"
price3 = 120
discount3 = 7
story3 = 120
size3 = "均码"

id4 = '04'
idName4 = "卫衣"
brand4 = "D"
price4 = 130
discount4 = 8
story4 = 110
size4 = "均码"

id5 = '05'
idName5 = "牛仔"
brand5 = "E"
price5 = 140
discount5 = 7
story5 = 110
size5 = "均码"

id6 = '06'
idName6 = "夹克"
brand6 = "F"
price6 = 150
discount6 = 8
story6 = 120
size6 = "均码"

print("===========================服装商店============================")
print("编号      名称      品牌      价格      折扣      库存      大小")
print("----------------------------------------------------------------")
print(id1, "     ", idName1, "  ", brand1, "     ", price1, "      ", discount1, "    ", story1, "     ", size1)
print(id2, "     ", idName2, "   ", brand2, "     ", price2, "      ", discount2, "    ", story2, "     ", size2)
print(id3, "     ", idName3, "    ", brand3, "     ", price3, "      ", discount3, "    ", story3, "     ", size3)
print(id4, "     ", idName4, "    ", brand4, "     ", price4, "      ", discount4, "    ", story4, "     ", size4)
print(id5, "     ", idName5, "    ", brand5, "     ", price5, "      ", discount5, "    ", story5, "     ", size5)
print(id6, "     ", idName6, "    ", brand6, "     ", price6, "      ", discount6, "    ", story6, "     ", size6)
print("----------------------------------------------------------------")
print("总金额￥ ", price1*discount1*0.1*story1+price2*discount2*0.1*story2+price3*discount3*0.1*story3+price4*discount4*0.1*story4+price5*discount5*0.1*story5+price6*discount6*0.1*story6)


date = ["1号", "2号", "3号", "4号", "5号", "6号", "7号", "8号", "9号", "10号", "11号", "12号", "13号", "14号", "15号", "16号", "17号", "18号", "19号", "20号", "21号", "22号", "23号", "24号", "25号", "26号", "27号", "28号", "29号", "30号"]

name = ["羽绒服", "牛仔裤", "风衣", "皮草", "T血", "衬衫"]
NUM = [7, 1, 6, 7, 4, 5]
prince = [49.3, 65.8, 86.3, 96.8, 135.9, 253.6]
kindNum = [239, 517, 292, 207, 469, 120]
story = [335, 500, 562, 600, 632, 855]

sellNum = [10, 24, 25, 35, 43, 45, 48, 57, 58, 60, 63, 69, 72, 78, 90, 120, 129, 140]


print("-----------------------------------------------------------")
print("日期   服装名称    价格/件    库存数量/个  销售量/每日")
print(date[0], "   ", name[0], "   ", prince[5], "      ", story[1], "      ",  sellNum[0])
print(date[1], "   ", name[1], "   ", prince[2], "      ", story[3], "      ",  sellNum[9])
print(date[2], "   ", name[2], "     ", prince[3], "      ", story[0], "      ",  sellNum[4])
print(date[3], "   ", name[3], "     ", prince[4], "      ", story[5], "      ",  sellNum[10])
print(date[4], "   ", name[4], "     ", prince[1], "      ", story[4], "      ",  sellNum[10])
print(date[5], "   ", name[5], "     ", prince[0], "      ", story[2], "      ",  sellNum[15])
print(date[6], "   ", name[1], "   ", prince[2], "      ", story[3], "      ",  sellNum[12])
print(date[7], "   ", name[0], "   ", prince[5], "      ", story[1], "      ",  sellNum[11])
print(date[8], "   ", name[1], "   ", prince[2], "      ", story[3], "      ",  sellNum[3])
print(date[9], "  ", name[0], "    ", prince[5], "      ", story[1], "      ",  sellNum[17])
print(date[10], "  ", name[1], "   ", prince[2], "      ", story[3], "      ",  sellNum[14])
print(date[11], "  ", name[3], "   ", prince[4], "      ", story[5], "      ",  sellNum[1])
print(date[12], "  ", name[4], "   ", prince[1], "      ", story[4], "      ",  sellNum[5])
print(date[13], "  ", name[2], "   ", prince[3], "      ", story[0], "      ",  sellNum[2])
print(date[14], "  ", name[1], "   ", prince[2], "      ", story[3], "      ",  sellNum[9])
print(date[15], "  ", name[4], "   ", prince[1], "      ", story[4], "      ",  sellNum[16])
print(date[16], "  ", name[0], "   ", prince[5], "      ", story[1], "      ",  sellNum[0])
print(date[17], "  ", name[2], "   ", prince[3], "      ", story[0], "      ",  sellNum[4])
print(date[18], "  ", name[4], "   ", prince[1], "      ", story[4], "      ",  sellNum[10])
print(date[19], "  ", name[1], "   ", prince[2], "      ", story[3], "      ",  sellNum[9])
print(date[20], "  ", name[3], "   ", prince[4], "      ", story[5], "      ",  sellNum[10])
print(date[21], "  ", name[2], "   ", prince[3], "      ", story[0], "      ",  sellNum[9])
print(date[22], "  ", name[4], "   ", prince[1], "      ", story[4], "      ",  sellNum[8])
print(date[23], "  ", name[1], "   ", prince[2], "      ", story[3], "      ",  sellNum[17])
print(date[25], "  ", name[4], "   ", prince[1], "      ", story[4], "      ",  sellNum[6])
print(date[26], "  ", name[3], "   ", prince[4], "      ", story[5], "      ",  sellNum[7])
print(date[27], "  ", name[0], "   ", prince[5], "      ", story[1], "      ",  sellNum[0])
print(date[28], "  ", name[4], "   ", prince[1], "      ", story[4], "      ",  sellNum[10])
print(date[29], "  ", name[2], "   ", prince[3], "      ", story[0], "      ",  sellNum[13])


print("羽绒服每件衣服的销售占比：￥", round(kindNum[0]/(kindNum[0] + kindNum[1] + kindNum[2] + kindNum[3] + kindNum[4]
                                          + kindNum[5])*100, 2), "%")
print("羽绒服每种衣服在本月的销售占比：￥", round(kindNum[0]*prince[5]/(kindNum[1]*prince[2]+kindNum[2]*prince[3] + kindNum[3]*prince[4]
                                                       + kindNum[4]*prince[1]+kindNum[5]*prince[0])*100, 2), "%")
print("本月总销售额：￥", round((kindNum[1]*prince[2]+kindNum[2]*prince[3]+kindNum[3]*prince[4]+kindNum[4]*prince[1]
                         + kindNum[5]*prince[0])*100*30, 2))



a = 56
b = 78

a = a + 22
b = b - 22

print(a, b)












