def fun(n, m):
    if n > m or n == 11 or n == 12:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n + 2, m) + fun(n * 3, m)
print(fun(1, 9) * fun(9, 30))