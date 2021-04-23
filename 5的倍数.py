a = [1,5,21,30,15,9,30,24]
m =[]
n = 0
while n <= len(a) - 1:
    if a[n]%5 == 0:
        m.append(a[n])
        n = n + 1
    else:
        n = n + 1
else:
    print("列表中5的倍数有：",m)
a = 0
s = 0
while True:
 if a <= len(m)-1:
    s = s + m[a]
    a = a + 1
 else:
    print("5的倍数的和为:", s)
    break
