for n in range (185311, 185331):
    k = 0
    g = []
    for d in range (1, int(n ** 0.5) + 1):
        if n % d == 0:
            k+=1
            g.append(d)
            if n // d != d:
                g.append(n//d)
    if len(g) == 4:
        print(g)