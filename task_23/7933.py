def fun(n, m):
    if n > 9:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n + 2, m) + fun(n * 2 - 1, m)
print(fun(2, 9))