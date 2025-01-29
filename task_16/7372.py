def fun(n):
    if n == 1:
        return 1
    if n >= 2:
        return fun(n-1) * n
print(fun(6))