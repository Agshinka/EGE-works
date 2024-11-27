a = '0123456789abcde'
g=[]
for x in a:
    for y in a:
        t = int('90' + x + '4' + y, 15) + int('91' + x + y + '2', 16)
        if t % 56 == 0:
            t = int(t//56)
            g.append(t)
            print(min(g))