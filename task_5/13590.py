for n in range (100, 1000):
    s = str(n)
    a1 = int(s[0]) * int(s[1])
    a2 = int(s[1]) * int(s[2])
    d1 = str(min(a1, a2))
    d2 = str(max(a1, a2))
    d = d2 + d1
    if d == '205':
        print(n)
        break