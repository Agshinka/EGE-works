for n in range (1000, 10000):
    n = str(n)
    a1 = int(n[0]) + int(n[1])
    a2 = int(n[1]) + int(n[2])
    a3 = int(n[2]) + int(n[3])
    r = sorted([a1, a2, a3])
    g = str(r[1]) + str(r[2])
    if g == '1515':
        print(n)