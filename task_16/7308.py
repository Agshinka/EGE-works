def fun(n):
    if n == 1:
        return 1
    if n > 1:
        return fun(n-1) + 2 ** (n-1)
print(fun(10))