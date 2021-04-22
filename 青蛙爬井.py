day = 0
h = 0
while True:
    h = h + 3
    day = day + 1
    if h < 20:
        h = h - 2

    else:
        print("青蛙在第",day,"天爬出来")
        break
