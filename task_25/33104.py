for n in range (int(289123456 * 0.5) + 1, int(389123457 * 0.5) + 1):
    g = []
    k = 0
    s = n * n
    for d in range (2, n + 1):
        if s % d == 0:
            k+=1
            g.append(d)
            if (s // d) != d:
                g.append(s // d)
            if len(g) > 3:
                break
    if len(g) == 3:
        print(s, max(g))