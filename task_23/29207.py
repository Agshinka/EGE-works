def fun(n, m):
    if n > 24 or n == 11:
        return 0
    if n == m:
        return 1
    else:
        return fun(n+1, m) + fun(n * 2, m)
print(fun(2, 12) * fun(12, 24))

def fun1(n, m):
    if n > 24 or n == 12:
        return 0
    if n == m:
        return 1
    else:
        return fun1(n+1, m) + fun1(n * 2, m)
print(fun1(2, 11) * fun1(11, 24))