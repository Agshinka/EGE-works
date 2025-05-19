a = '01234567'
for x in a:
    for y in a:
        d = int(x + '01' + y + '4', 9) + int(x + y + '544', 8)
        if d % 89 == 0:
            print(d / 89)