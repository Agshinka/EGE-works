def fun(n):
    if n == 1:
        return 1
    else:
        return fun(n-1) * fun(n-1) - fun(n-1) * n + 2 * n
print(fun(4)) 