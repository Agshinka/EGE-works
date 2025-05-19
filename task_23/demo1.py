def fun(n, m):
    if n < 2:
        return 0
    if n == m:
        return 1
    else:
        return fun(n - 2, m) + fun(n // 2, m)
print(fun(38, 16) * fun(16, 2))