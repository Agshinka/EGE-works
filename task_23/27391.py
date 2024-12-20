def fun(n, m):
    if n > m:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 2, m) + fun(n * 2, m)
print(fun(1, 14) * fun(14, 30))