def fun(n, m):
    if n > 15:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n + 2, m) + fun(n + 4, m)
print(fun(1, 8) * fun(8, 15))