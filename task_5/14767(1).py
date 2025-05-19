for n in range (1000, 10000):
    s = str(n)
    a1 = int(s[0]) + int(s[1])
    a2 = int(s[1]) + int(s[2])
    a3 = int(s[2]) + int(s[3])
    r = sorted([a1, a2, a3])
    e = str(r[1]) + str(r[2])
    if e == '613':
        print(n)
