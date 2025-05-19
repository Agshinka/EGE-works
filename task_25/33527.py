def fun(n):
    b = set()
    j=[]
    for x in range (1, int(n ** 0.5) + 1):
        if n % x == 0:
            b.add(x)
            b.add(n // x)
    b = list(b)
    for g in range (len(b)):
        if b[g] % 2 == 0:
            j.append(b[g])
    return sorted(j)

# print(fun(32))

for n in range (101_000_000, 102_000_001):
    if len(fun(n)) == 3:
        print(n)