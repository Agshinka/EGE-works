def fun(n):
    b = []
    for x in range (2, n):
        if n % x == 0:
            b.append(n // x)
    return sorted(b)

def fun1(n):
    s = fun(n)
    if len(s) == 0:
        b = 0
    else:
        b = min(s) ** 2 + max(s) ** 2
        if 