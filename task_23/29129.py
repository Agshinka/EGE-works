def fun(n, m):
    if n > m:
        return 0
    elif n == m:
        return 1
    else:
        return fun(n+1, m) + fun(n * 2, m)
print(fun(3, 13) * fun(13, 30) * fun(30, 60))