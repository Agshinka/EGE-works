def fun(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n * 2, m) + fun(n * 3, m)
print(fun(2, 15) * fun(15, 30))