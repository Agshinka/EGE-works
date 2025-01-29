for n in range (100, 1000):
    s = str(n)
    a1 = int(s[0]) + int(s[1])
    a2 = int(s[1]) + int(s[2])
    a = sorted([a1, a2])
    d = str(max(a)) + str(min(a))
    if d == '1711':
        print(n)