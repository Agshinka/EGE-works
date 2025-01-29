for n in range (1000, 10000):
    s = str(n)
    a1 = int(s[0]) + int(s[1])
    a2 = int(s[1]) + int(s[2])
    a3 = int(s[2]) + int(s[3])
    a = sorted([a1, a2, a3])
    d = str(a[1]) + str(a[2])
    if d == '1215':
        print(n)
        break