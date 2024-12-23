def fun(n, m):
    if n < m or n == 10 or n == 15:
        return 0
    elif n == m:
        return 1
    elif n % 2 == 0 and n % 3 == 0:
        return fun(n-1, m) + fun(n // 2, m) + fun(n // 3, m)
    elif n % 2 == 0:
        return fun(n-1, m) + fun(n // 2, m)
    elif n % 3 == 0:
        return fun(n-1, m) + fun(n // 3, m)
    else:
        return fun(n - 1, m)
print(fun(22, 1))