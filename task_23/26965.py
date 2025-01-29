def fun(n, m):
    if n > m:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n + 2, m) + fun(n * 2, m)
print(fun(4, 11) * fun(11, 13))