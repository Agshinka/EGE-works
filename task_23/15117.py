def fun(n, m):
    if n > m or n == 15:
        return 0
    elif n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n + 2, m)
print(fun(3, 9) * fun (9, 20))