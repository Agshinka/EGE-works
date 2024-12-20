def fun(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n+2, m) + fun(n+6, m)
print(fun(21, 30))