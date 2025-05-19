def fun(n):
    b = []
    for x in range (2, n):
        if n % x == 0:
            b.append(n // x)
    return sorted(b)

for n in range (1_200_001, 1_250_000):
    d = [i for i in fun(n) if len(fun(i)) == 0]
    if len(d) != 0:
        if (min(d) + max(d)) > 2000:
            if (min(d) + max(d)) % 10 == 8:
                print(n, (min(d) + max(d)))