def fun(n, m):
    if n > m or n == 30:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n * 2, m) + fun(n * 3,m)
print(fun(2, 12) * fun(12, 36))