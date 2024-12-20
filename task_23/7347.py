def fun(n, m):
    if n > m:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n * 2, m) + fun(2 * n + 1, m) + fun(n * 10, m)
print(fun(1, 14))