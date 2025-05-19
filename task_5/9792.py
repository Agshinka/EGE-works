for n in range (100, 1000):
    s = str(n)
    a1 = int(s[0]) * int(s[1])
    a2 = int(s[1]) * int(s[2])
    e = sorted([a1, a2])
    d = str(e[0]) + str(e[1])
    if d == '621':
        print(n)