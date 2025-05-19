def fun(n):
    b = []
    for x in range (1, n + 1):
        if n % x == 0:
            b.append(n // x)
    return sorted(b)

for n in range (489421, 489441):
    if len(fun(n)) == 4:
        print(fun(n))