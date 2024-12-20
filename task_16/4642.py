def fun(n):
    if n == 1:
        return 3
    else:
        return fun(n-1) * (n-1)
print(fun(6))
