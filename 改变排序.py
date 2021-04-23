l = [1,2,3,4,5,6,7,8,9]
i= 0
while i < len(l):
    j = 0
    while j < len(l) - 1:
        if l[j + 1] > l[j]:
            l[j], l[j + 1] = l[j + 1], l[j]
        j += 1
    i += 1
print(l)




