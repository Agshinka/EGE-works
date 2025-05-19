def fun(n):
    d = set()
    for x in range (2, int(n ** 0.5) + 1):
        if n % x == 0:
            d.add(x)
            d.add(n // x)
    return sorted(d)

k=0
for g in range (112_500_000, 112_550_000 + 1):
    delit = fun(g)
    if len(delit) >= 2:
        k = delit[-2] + delit[-1]
        if k % 10000 == 1214:
            print(g)