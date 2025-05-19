def fun(n):
    b = set()
    for x in range (2, int(n ** 0.5) + 1):
        if n % x == 0:
            b.add(x)
            b.add(n // x)
    b = sorted(list(b))
    return b

for n in range(460000001, 460100001):
    if len(fun(n)) >= 5:
        print(fun(n)[-5])

# a = [2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500]
# print(a[-5])