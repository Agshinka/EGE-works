def fun(n, m):
    if n == 14 or n > m:
        return 0
    elif n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n + 2, m)
print(fun(2, 9) * fun(9, 18))