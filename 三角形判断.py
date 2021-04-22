a = int(input("请输入第一条边的边长："))
b = int(input("请输入第二条边的边长："))
c = int(input("请输入第三条边的边长："))
info = '''
***********三角形的边长********
a: %s,
b: %s,
c: %s
'''
print(info   %   (a,b,c))
while a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("是等边三角形")
        break
    elif a == b or a == c or b == c:
        print("是等腰三角形")
        break
    elif (a * a + b * b == c * c) or (b * b + c * c == a * a) or (a * a + c * c == b * b):
        print("是直角三角形")
        break
    else:
       print("是普通三角形")
       break
else:
 print("不是三角形")

