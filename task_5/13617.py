for n in range (100, 1000):
    s = str(n)
    a1 = int(s[0]) * int(s[1])
    a2 = int(s[1]) * int(s[2])
    d = sorted([a1, a2])
    f = str(d[1]) + str(d[0])
    if f == '123':
        print(n)
