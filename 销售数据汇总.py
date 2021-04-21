date1 = "1号"
name1 = "羽绒服"
jg1 = 253.6
num1 = 500
xl1 = 10

date2 = "2号"
name2 = "牛仔裤"
jg2 = 86.3
num2 = 600
xl2 = 60

date3 = "3号"
name3 = "风衣"
jg3 = 96.8
num3 = 335
xl3 = 43

date4 = "4号"
name4 = "皮草"
jg4 = 135.9
num4 = 855
xl4 = 63

date5 = "5号"
name5 = "T血"
jg5 = 65.8
num5 = 632
xl5 = 63

date6 = "6号"
name6 = "衬衫"
jg6 = 49.3
num6 = 562
xl6 = 120

date7 = "7号"
name7 = "牛仔裤"
jg7 = 86.3
num7 = 600
xl7 = 72

date8 = "8号"
name8 = "羽绒服"
jg8 = 253.6
num8 = 500
xl8 = 69

date9 = "9号"
name9 = "牛仔裤"
jg9 = 86.3
num9 = 600
xl9 = 35

date10 = "10号"
name10 = "羽绒服"
jg10 = 253.6
num10 = 500
xl10 = 140

date11 = "11号"
name11 = "牛仔裤"
jg11 = 86.3
num11 = 600
xl11 = 90

date12 = "12号"
name12 = "皮草"
jg12 = 135.9
num12 = 855
xl12 = 24

date13 = "13号"
name13 = "T血"
jg13 = 65.8
num13 = 632
xl13 = 45

date14 = "14号"
name14 = "风衣"
jg14 = 96.8
num14 = 335
xl14 = 25

date15 = "15号"
name15 = "牛仔裤"
jg15 = 86.3
num15 = 600
xl15 = 60

date16 = "16号"
name16 = "T血"
jg16 = 65.8
num16 = 632
xl16 = 129

date17 = "17号"
name17 = "羽绒服"
jg17 = 253.6
num17 = 500
xl17 = 10

date18 = "18号"
name18 = "风衣"
jg18 = 96.8
num18 = 335
xl18 = 43

date19 = "19号"
name19 = "T血"
jg19 = 65.8
num19 = 632
xl19 = 63

date20 = "20号"
name20 = "牛仔裤"
jg20 = 86.3
num20 = 600
xl20 = 60

date21 = "21号"
name21 = "皮草"
jg21 = 135.9
num21 = 855
xl21 = 63

date22 = "22号"
name22 = "风衣"
jg22 = 96.8
num22 = 335
xl22 = 60

date23 = "23号"
name23 = "T血"
jg23 = 65.8
num23 = 632
xl23 = 58

date24 = "24号"
name24 = "牛仔裤"
jg24 = 86.3
num24 = 600
xl24 = 140

date25 = "25号"
name25 = "T血"
jg25 = 65.8
num25 = 632
xl25 = 48

date26 = "26号"
name26 = "风衣"
jg26 = 96.8
num26 = 335
xl26 = 43

date27 = "27号"
name27 = "皮草"
jg27 = 135.9
num27 = 855
xl27 = 57

date28 = "28号"
name28 = "羽绒服"
jg28 = 253.6
num28 = 500
xl28 = 10

date29 = "29号"
name29 = "T血"
jg29 = 65.8
num29 = 632
xl29 = 63

date30 = "30号"
name30 = "风衣"
jg30 = 96.8
num30 = 335
xl30 = 78

ZXL = (xl1 + xl2 + xl3 + xl4 + xl5 + xl6 + xl7 + xl8 +xl9 + xl10
       + xl11 + xl12 + xl13 + xl14 + xl15 + xl16 + xl17 + xl18 + xl19 + xl20
       + xl21 + xl22 + xl23 + xl24 + xl25 + xl26 + xl27 + xl28 +xl29 + xl30)
ZXSE = (jg1 * (xl1 + xl8 + xl10 + xl17 + xl28) + jg2 *
               (xl2 + xl7 + xl9 + xl11 + xl15 + xl20 + xl24) +
               jg3 * (xl3 + xl14 + xl18 + xl22 + xl26 + xl30) +
               jg4 * (xl4 + xl12 + xl21 + xl27) + jg5 * (xl5 +
                xl13 + xl16 + xl19 + xl23 + xl25 + xl29) + jg6 * xl6)

print("---------12月份衣服销售数据---------")
print("日期   服装名称   价格   库存数量   销售量")
print(date1,"\t",name1,"\t",jg1,"\t",num1,"\t",xl1)
print(date2,"\t",name2,"\t",jg2,"\t",num2,"\t",xl2)
print(date3,"\t",name3,"\t",jg3,"\t",num3,"\t",xl3)
print(date4,"\t",name4,"\t",jg4,"\t",num4,"\t",xl4)
print(date5,"\t",name5,"\t",jg5,"\t",num5,"\t",xl5)
print(date6,"\t",name6,"\t",jg6,"\t",num6,"\t",xl6)
print(date7,"\t",name7,"\t",jg7,"\t",num7,"\t",xl7)
print(date8,"\t",name8,"\t",jg8,"\t",num8,"\t",xl8)
print(date9,"\t",name9,"\t",jg9,"\t",num9,"\t",xl9)
print(date10,"\t",name10,"\t",jg10,"\t",num10,"\t",xl10)
print(date11,"\t",name11,"\t",jg11,"\t",num11,"\t",xl11)
print(date12,"\t",name12,"\t",jg12,"\t",num12,"\t",xl12)
print(date13,"\t",name13,"\t",jg13,"\t",num13,"\t",xl13)
print(date14,"\t",name14,"\t",jg14,"\t",num14,"\t",xl14)
print(date15,"\t",name15,"\t",jg15,"\t",num15,"\t",xl15)
print(date16,"\t",name16,"\t",jg16,"\t",num16,"\t",xl16)
print(date17,"\t",name17,"\t",jg17,"\t",num17,"\t",xl17)
print(date18,"\t",name18,"\t",jg18,"\t",num18,"\t",xl18)
print(date19,"\t",name19,"\t",jg19,"\t",num19,"\t",xl19)
print(date20,"\t",name20,"\t",jg20,"\t",num20,"\t",xl20)
print(date21,"\t",name21,"\t",jg21,"\t",num21,"\t",xl21)
print(date22,"\t",name22,"\t",jg22,"\t",num22,"\t",xl22)
print(date23,"\t",name23,"\t",jg23,"\t",num23,"\t",xl23)
print(date24,"\t",name24,"\t",jg24,"\t",num24,"\t",xl24)
print(date25,"\t",name25,"\t",jg25,"\t",num25,"\t",xl25)
print(date26,"\t",name26,"\t",jg26,"\t",num26,"\t",xl26)
print(date27,"\t",name27,"\t",jg27,"\t",num27,"\t",xl27)
print(date28,"\t",name28,"\t",jg28,"\t",num28,"\t",xl28)
print(date29,"\t",name29,"\t",jg29,"\t",num29,"\t",xl29)
print(date30,"\t",name30,"\t",jg30,"\t",num30,"\t",xl30)
print("总销售额：￥",(jg1 * (xl1 + xl8 + xl10 + xl17 + xl28) + jg2 *
               (xl2 + xl7 + xl9 + xl11 + xl15 + xl20 + xl24) +
               jg3 * (xl3 + xl14 + xl18 + xl22 + xl26 + xl30) +
               jg4 * (xl4 + xl12 + xl21 + xl27) + jg5 * (xl5 +
                xl13 + xl16 + xl19 + xl23 + xl25 + xl29) + jg6 * xl6))
print("羽绒服的销售占比为：",round ((xl1 + xl8 + xl10 + xl17 + xl28)/ZXL,2),
      "牛仔裤的销售占比为：",round ((xl2 + xl7 + xl9 + xl11 + xl15 + xl20 + xl24)/ZXL,2),
      "风衣的销售占比为：",round ((xl3 + xl14 + xl18 + xl22 + xl26 + xl30)/ZXL,2),
      "皮草的销售占比为：",round ((xl4 + xl12 + xl21 + xl27)/ZXL,2),
      "T血的销售占比为：",round((xl5 + xl13 + xl16 + xl19 + xl23 + xl25 + xl29)/ZXL,2),
      "衬衫的销售占比为：",round(xl6/ZXL,2))
print("羽绒服的销售额占比为：",(round(jg1 * (xl1 + xl8 + xl10 + xl17 + xl28)/ZXSE,2)))
print("牛仔裤的销售额占比为：",(round(jg2 * (xl2 + xl7 + xl9 + xl11 + xl15 + xl20 + xl24)/ZXSE,2)))
print("风衣的销售额占比为：",(round(jg3 * (xl3 + xl14 + xl18 + xl22 + xl26 + xl30)/ZXSE,2)))
print("皮草的销售额占比为：",(round(jg4 * (xl4 + xl12 + xl21 + xl27)/ZXSE,2)))
print("T血的销售额占比为：",(round(jg5 * (xl5 + xl13 + xl16 + xl19 + xl23 + xl25 + xl29)/ZXSE,2)))
print("衬衫的销售额占比为：",(round(jg6 * xl6/ZXSE,2)))