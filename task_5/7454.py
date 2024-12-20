for n in range (1000, 10000):
    s = str(n)
    a1 = int(s[0]) + int(s[1])
    a2 = int(s[2]) + int(s[3])
    d = str(min(a1, a2))
    d1 = str(max(a1, a2))
    d3 = d1 + d
    if d3 == '1311':
        print(n)