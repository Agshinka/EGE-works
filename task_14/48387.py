a = '0123456789a'
for x in a:
    for y in a:
        d = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
        if d % 305 == 0:
            print(int(d // 305))