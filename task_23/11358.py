def fum(n, m): 
    if n > m:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n + 2, m) + fun(n * 2, m)
print(fun(3, 10) * f(10, 12))