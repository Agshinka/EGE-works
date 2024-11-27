a = '0123456789ab'
b = []
for x in a:
    t = int('2AB' + x, 12) + int(x + '8E', 17)
    if t % 27 == 0:
        t = int(t//27)
        b.append(t)
        print(min(b))