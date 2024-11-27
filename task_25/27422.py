for n in range (174457, 174506):
    k=0
    g=[]
    for d in range (2, (n//2 + 1)):
        if n % d == 0:
            k += 1
            g.append(d)
            if k > 2:
                break
    if k == 2:
        print(g)