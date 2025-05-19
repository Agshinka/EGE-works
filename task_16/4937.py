def fun(n):
    if n == 1:
        return 1
    if n == 1:
        return 2
    if n > 2:
        return fun(n-2) * (n-1)
print(fun(7))