def fun(n, m):
    if n > m or n == 24:
        return 0
    elif n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(2 * n + 1, m)
print(fun(1, 25))