def fun(n, m):
    if n > 15:
        return 0
    if n == m:
        return 1
    else:
        return fun(n+1, m) + fun(n+3, m)
print(fun(2, 15))