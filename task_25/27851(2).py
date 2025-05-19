def fun(n):
    b = set()
    for x in range (2, n):
        if n % x == 0:
            b.add(n // x)
    return sorted(b)

for n in range (210_235, 210_300 + 1):
    if len(fun(n)) == 4:
        print(fun(n))