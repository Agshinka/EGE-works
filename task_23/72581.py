def fun(n, m):
    if n < m:
        return 0
    elif n == m:
        return 1
    else:
        return fun(n - 2, m) + fun(n // 2, m) + fun(n // 3, m)
print(fun(40, 20) * fun(20, 4))