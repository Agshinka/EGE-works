def fun(n, m):
    if n > m or n == 9:
        return 0
    if n == m:
        return 1
    else:
        return fun(n + 1, m) + fun(n * 2, m)
    
def fun1(n, m):
    if n > m or n == 10:
        return 0
    if n == m:
        return 1
    else:
        return fun1(n + 1, m) + fun1(n * 2, m)
print(fun(1, 10) * fun(10, 20) + fun1(1, 9) * fun1(9, 20))