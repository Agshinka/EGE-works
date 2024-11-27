pos = 0
for n in range (245690, 245757):
    pos += 1
    k = 0
    g = []
    for d in range (2, n // 2 + 1):
        if n % d == 0:
            k+=1
            g.append(d)
            if k > 0:
                break
    if k == 0:
        print(pos, n)