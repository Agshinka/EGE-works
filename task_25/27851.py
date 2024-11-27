for n in range (210235, 210301):
    k = 0
    g = []
    for d in range (2, n // 2 + 1):
        if n % d == 0:
            k += 1
            g.append(d)
            if k > 4:
                break
    if k == 4:
        print(g)