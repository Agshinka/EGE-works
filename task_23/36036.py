def fun(n, m):
    if n < m:
        return 0
    if n == m:
        return 1
    else:
        return fun(n - 2, m) + fun(n - 5, m)
print(fun(23, 2))