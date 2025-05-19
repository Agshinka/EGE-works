def fun(n):
    b = set()
    for x in range (2, int(n ** 0.5) + 1):
        if n % x == 0:
            b.add(x)
            b.add(n // x)
    b = sorted(list(b))
    if len(b) < 2:
        return 0
    else:
        return (b[-1] + b[-2])


for n in range (10_000_000, 10_300_001):
    g=[]
    if fun(n) > 0 and fun(n) < 10000:
        g.append(fun(n))
        print(sorted(g))
